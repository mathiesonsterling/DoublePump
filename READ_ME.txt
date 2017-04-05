What is double pump?
    doublepump is an extremely lightweight library to allow tasks to be repeated until complete (or failed), and also
    make sure any dependent tasks have been completed first.  It aims to fill a spot between great frameworks such as
    Luigi or Chef, which are often too heavy for some uses, and also demand a process to be run separately.  Instead
    DoublePump is designed to be embedded in other programs.

    Tasks answer a few simple questions -
       is what I'm trying to do done?
       how do I make it done?
       what do I need done before I can act?

    Users can easily add tasks by extending the Task class.  They should then implement the
    get_status method (is what I'm trying to do done?), and the do method (how do I make it done).

    Tasks by default will attempt 3 times before failing, with a delay of 10ms in between.  These values are per task,
    so that more complex tasks (such as provisioning a machine)

    Built-in tasks
       A few tasks have been built in for ease of use.  These include . . . .



later features to be added:
  - add paralizable task paths when possible
  - dynamic generation of tasks from code rather than instance
  - repeatable tasks?
  - per task type resource
