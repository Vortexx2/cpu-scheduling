import logging
from typing import List
from utilities import *


def fcfs(processes: List[Process]) -> Gantt:
  """
  Executes `processes` according to the FCFS algorithm.

  Should return a list of SubProcess, which is the final result.
  """
  gantt = Gantt()

  if not len(processes):
    return gantt

  totalBurst = total_burst(processes)
  # print(f"total burst: {totalBurst}")
  time = 0

  while totalBurst:
    earliestProc = None

    for proc in processes:
      if (not proc.isComplete()) and (not earliestProc):
        # print("a")
        earliestProc = proc

      if (not proc.isComplete()) and proc.arrTime < earliestProc.arrTime:
        earliestProc = proc

    # log error if there is discrepancy
    if not earliestProc:
      logging.error("Total Burst != 0 but all processes finished execution")

    currentSubProcess = SubProcess(time, earliestProc.burst, earliestProc)
    currentSubProcess.execute(gantt)
    time += earliestProc.burst
    totalBurst -= earliestProc.burst

  return gantt


if __name__ == "__main__":

  # define processes
  processes = temp_proc_list()

  gantt = fcfs(processes)
  print(gantt)
