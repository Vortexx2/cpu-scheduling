from typing import List

from numpy import Infinity
from utilities import *


def sjf(processes: List[Process]) -> Gantt:
  gantt = Gantt()

  if not len(processes):
    return gantt

  time = 0
  totalBurst = total_burst(processes)

  while totalBurst:
    # next process to execute
    nextExec = None

    for proc in processes:

      if not proc.isComplete():

        if proc.arrTime <= time:
          if not nextExec:
            nextExec = proc

          if proc.burst < nextExec.burst:
            nextExec = proc

    nextExecSub = SubProcess(time, nextExec.burst, nextExec)
    nextExecSub.execute(gantt)
    time += nextExec.burst
    totalBurst -= nextExec.burst

  return gantt


def preemp_sjf(processes: List[Process]) -> Gantt:
  gantt = Gantt()

  if not len(processes):
    return gantt

  time = 0
  totalBurst = total_burst(processes)

  while totalBurst:
    nextExec = None

    for proc in processes:
      if not proc.isComplete():
        if proc.arrTime <= time:

          if not nextExec:
            nextExec = proc

          if proc.timeLeft() < nextExec.timeLeft():
            nextExec = proc

    nextExecSub = SubProcess(time, 1, nextExec)
    nextExecSub.execute(gantt)

    time += 1
    totalBurst -= 1

  return gantt


if __name__ == "__main__":
  processes = temp_proc_list()

  # gantt = sjf(processes)
  gantt = preemp_sjf(processes)

  print(gantt)
