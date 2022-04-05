from typing import Optional, List

# ------ defining all of the utility methods -------


def temp_proc_list():
  """ Returns the proc list described in the assignment doc file """
  processes = []
  pids = ['p1', 'p2', 'p3', 'p4']
  aTimes = [0, 4, 3, 2]
  bTimes = [8, 5, 2, 1]
  prios = [4, 2, 1, 3]  # higher no. indicates lower priority
  # prios = []

  procCreation = (pids, aTimes, bTimes, prios) if prios else (
      pids, aTimes, bTimes)

  for tup in zip(*procCreation):
    processes.append(Process(*tup))

  return processes


def total_burst(processes: List["Process"]) -> int:
  totalBurst = 0
  for proc in processes:
    totalBurst += proc.burst

  return totalBurst


# ------- defining all of the utility classes -------


class Process:
  """
  Define basic structure of a process
  """

  def __init__(self, pid: str, arrTime: int, burst: int, prio: Optional[int] = None) -> None:
    """
    Each process will have a pid, arrTime, burst. Priority of the process is optional.
    Each process also has a completed attribute which shows amount of process completed.
    """
    self.pid, self.arrTime, self.burst = pid, arrTime, burst

    self.prio = prio

    self._completed = 0

  def isComplete(self) -> bool:
    """ Returns if process has completed execution or not """
    return self.completed == self.burst

  def timeLeft(self) -> int:
    """ Returns the amount of seconds left of execution of process """
    return self.burst - self.completed

  @property
  def completed(self):
    return self._completed

  @completed.setter
  def completed(self, new_comp):
    if new_comp < 0:
      self._completed = 0

    elif new_comp > self.burst:
      self._completed = self.burst

    else:
      self._completed = new_comp

  def __str__(self) -> str:
    return f"Process id: {self.pid},\t Arrival Time: {self.arrTime},\t Burst Time: {self.burst},\t Priority: {self.prio if self.prio else 'No priority'}"


class SubProcess():
  """
  SubProcess where we define when the subprocess started and when it ended current execution (not necessarily execution of the whole process, like in preemptive algorithms)
  """

  def __init__(self, startTime: int, currBurst: int, proc: Process) -> None:
    self.proc = proc

    self.start, self.currBurst = startTime, currBurst

  def execute(self, gantt: "Gantt"):

    self.proc.completed += self.currBurst
    gantt.add(self, self.currBurst)


class Gantt:
  """
  Define a gantt chart to easily display the final process scheduling
  """

  def __init__(self) -> None:
    self.gArr: List[SubProcess] = []
    self.totalExecTime = 0

  def add(self, subProc: SubProcess, execTime: int):
    self.gArr.append(subProc)
    self.totalExecTime += execTime

  # def combineSubProcesses(self) -> None:
  #   collapsedArr = []
  #   prevSub = None

  #   for subp in self.gArr:
  #     if subp.proc.pid != prevSub.proc.pid:
  #       newProc = Process(subp.proc.pid, subp.proc.arrTime, subp.proc.burst, subp.proc.prio)
  #       newProcSub = SubProcess(subp.)
  #       collapsedArr.append(subp)
  #       prevSub = subp

  #   self.gArr = collapsedArr

  def __str__(self) -> str:
    res = ""
    if not self.gArr:
      res = "Gantt chart is empty"

    else:
      for subProc in self.gArr:
        res += f"Process {subProc.proc.pid} executed for {subProc.currBurst} seconds from {subProc.start} to {subProc.start + subProc.currBurst}\n"

    return res
