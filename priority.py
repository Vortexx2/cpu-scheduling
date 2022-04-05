from typing import List, Optional

from utilities import *


def priority(processes: List[Process]) -> Gantt:
  gantt = Gantt()

  if not len(processes):
    return gantt

  totalBurst = total_burst(processes)
  time = 0

  while totalBurst:
    nextExec = None

    for proc in processes:

      if not proc.isComplete():
        if proc.arrTime <= time:

          if not nextExec:
            nextExec = proc

          if proc.prio < nextExec.prio:
            nextExec = proc

    nextExecSub = SubProcess(time, nextExec.burst, nextExec)
    nextExecSub.execute(gantt)
    time += nextExec.burst
    totalBurst -= nextExec.burst

  return gantt


def preemp_priority(processes: List[Process]) -> Gantt:
  gantt = Gantt()

  if not len(processes):
    return gantt

  totalBurst = total_burst(processes)
  time = 0

  while totalBurst:
    nextExec = None

    for proc in processes:

      if not proc.isComplete():

        if proc.arrTime <= time:

          if not nextExec:
            nextExec = proc

          if proc.prio < nextExec.prio:
            nextExec = proc

    nextExecSub = SubProcess(time, 1, nextExec)
    nextExecSub.execute(gantt)
    time += 1
    totalBurst -= 1

  return gantt


if __name__ == "__main__":

  processes = temp_proc_list()

  gantt = preemp_priority(processes)
  print(gantt)
