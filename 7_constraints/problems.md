# Modelling CP problems

[« Previous](.) \| [Up ↑](.) \| [Next »](./theory)

## Workforce scheduling

Consider a bus company scheduling drivers for its buses. The requirement for
buses varies from hour to hour because of customer demand. For example, four
buses must run from midnight to 4 a.m., while eight buses must run from 4 a.m.
until 8 a.m. We assume that the bus requirements are the same every day.

The problem is to determine how many drivers to schedule at each starting time
to cover the requirements for buses. Drivers work eight hour shifts, e.g. a
driver starting at time 0 can drive a bus from time 0 to 8. A driver scheduled
to start at time 20 works for the final four hours of the day and the first
four hours of the next day.

Although a driver can be hired for an eight hour period, there is no requirement
that he drives a bus for the entire period. However, he cannot be on duty during
two consecutive shifts.

The goal is to minimize how many drivers to hire during a week.

## Productivity rate

Consider an aircraft manufacturing company. With practice and experience, they
have optimised their production line and comfortably assemble 48 aircraft per
month. Yet, they have recently accepted a significant number of orders and need
to increase their production accordingly: stakeholders set an objective of 52
aircraft per month.

- Each aircraft should pass through different workstations;
- Specific tasks are to be performed by qualified human operators;
- Some critical tasks are constrained by precedence relationships (i.e., they
  must be performed before others);
- Some critical tasks require specific equipments only available in limited
  quantity; moreover, these equipments cannot be moved from a workstation to
  another and are only be handled by operators who followed an appropriate
  training;
- Operators need time to move from a workstation to another;
- Few equipments need to cool down before being used again after some
  particularly demanding tasks;
- Schedules for operators are subject to labour laws regulating consecutive
  working hours.

The goal is to find an efficient scheduling for tasks, operators and
workstations such that 52 aircraft per month are assembled.

<div class="alert alert-warning"><b>Exercice:</b><br>
Write the set of variables for each of the two introductory problems. Write the constraints and objective function.
</div>

<div class="alert alert-danger"><b>Scope of the course</b><br>
These problems are typical scheduling problems that are well fit for the
Constraint Programming paradigm. The core concept behind constraint programming
is basic: define variables, domains, and constraints that describe relationships
with your variables. If relevant, you may define an objective function to
minimise (resp. maximise)
</div>

Basic arithmetic is provided _for free_, as well as some human-friendly
convenient tools. In particular, Constraint Programming comes with:

- disjunctions of (basic) constraints, implications;
- array-indexing with variables, getting the smallest element of an array of
  variables, etc.;
- global constraints with specific propagation methods optimised for resolution
  (`alldifferent`, `cardinality`, `precedence`, etc.)

[« Previous](.) \| [Up ↑](.) \| [Next »](./theory)
