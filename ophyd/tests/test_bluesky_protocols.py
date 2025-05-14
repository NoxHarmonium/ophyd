import pytest

imports = ""
imports += "import ophyd;"
imports += "from ophyd import flyers, sim;"
imports += "hw = sim.hw();"


def test_configurable(run_typecheck):
    cmd = imports + "from bluesky.protocols import Configurable;"
    run_typecheck(cmd + "foo: Configurable = hw.motor1")
    run_typecheck(cmd + "foo: Configurable = ophyd.Device(name='test')")
    run_typecheck(cmd + "foo: Configurable = hw.signal")


def test_triggerable(run_typecheck):
    cmd = imports + "from bluesky.protocols import Triggerable;"
    run_typecheck(cmd + "foo: Triggerable = hw.det")


def test_checkable(run_typecheck):
    cmd = imports + "from bluesky.protocols import Checkable;"
    run_typecheck(cmd + "foo: Checkable = hw.motor1")
    run_typecheck(cmd + "foo: Checkable = ophyd.Device(name='test')")


def test_hashints(run_typecheck):
    cmd = imports + "from bluesky.protocols import HasHints;"
    run_typecheck(cmd + "foo: HasHints = ophyd.Signal(name='test')")


def test_flyable(run_typecheck):
    cmd = imports + "from bluesky.protocols import Flyable;"
    run_typecheck(cmd + "foo: Flyable = hw.flyer1")
    run_typecheck(cmd + "foo: Flyable = sim.TrivialFlyer()")


def test_movable(run_typecheck):
    cmd = imports + "from bluesky.protocols import Movable;"
    run_typecheck(cmd + "foo: Movable = hw.motor1")
    run_typecheck(cmd + "foo: Movable = hw.flyer1")
    run_typecheck(cmd + "foo: Movable = ophyd.Component(ophyd.Signal, 'prefix')")
    run_typecheck(cmd + "foo: Movable = ophyd.Device(name='test')")
    run_typecheck(cmd + "foo: Movable = ophyd.Component(ophyd.Signal, 'prefix')")


def test_pausable(run_typecheck):
    cmd = imports + "from bluesky.protocols import Pausable;"
    run_typecheck(cmd + "foo: Pausable = hw.motor1")
    run_typecheck(cmd + "foo: Pausable = ophyd.Device(name='test')")


def test_readable(run_typecheck):
    cmd = imports + "from bluesky.protocols import Readable;"
    run_typecheck(cmd + "foo: Readable = hw.motor1")
    run_typecheck(cmd + "foo: Readable = ophyd.Device(name='test')")
    run_typecheck(cmd + "foo: Readable = hw.signal")


def test_stageable(run_typecheck):
    cmd = imports + "from bluesky.protocols import Stageable;"
    run_typecheck(cmd + "foo: Stageable = hw.motor1")
    run_typecheck(cmd + "foo: Stageable = ophyd.Device(name='test')")


def test_status(run_typecheck):
    cmd = imports + "from bluesky.protocols import Status;"
    run_typecheck(cmd + "foo: Status = ophyd.status.Status()")
    run_typecheck(cmd + "foo: Status = ophyd.status.StatusBase()")


def test_stoppable(run_typecheck):
    cmd = imports + "from bluesky.protocols import Stoppable;"
    run_typecheck(cmd + "foo: Stoppable = hw.motor1")
    run_typecheck(cmd + "foo: Stoppable = hw.flyer1")


# TODO: Ophyd signature is incompatible with bluesky protocol
# (extra parameters, returns int instead of None, different parameter names)
# Pyright is stricter and picks this up. Disabled for now
@pytest.mark.skip()
def test_subscribable(run_typecheck):
    cmd = imports + "from bluesky.protocols import Subscribable;"
    run_typecheck(cmd + "foo: Subscribable = hw.signal")
    run_typecheck(cmd + "foo: Subscribable = ophyd.Signal(name='test')")
    run_typecheck(cmd + "foo: Subscribable = ophyd.Device(name='test')")
    run_typecheck(cmd + "foo: Subscribable = hw.motor1")
    run_typecheck(cmd + "foo: Subscribable = hw.flyer1")


if __name__ == "__main__":
    test_configurable()
    test_triggerable()
    test_checkable()
    test_hashints()
    test_flyable()
    test_movable()
    test_pausable()
    test_readable()
    test_stageable()
    test_status()
    test_stoppable()
    # test_subscribable() # Disabled temporarily, see test
