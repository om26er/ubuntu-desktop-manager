import tempfile

import dbus
import pyscreenshot

GREETER_DBUS_NAME = 'org.gnome.ScreenSaver'
UNITY_SESSION_DBUS_PATH = '/com/canonical/Unity/Session'
UNITY_SESSION_DBUS_INTERFACE = 'com.canonical.Unity.Session'


def get_greeter_dbus_interface():
    """Return the unity greeter dbus interface."""
    bus = dbus.SessionBus()
    dbus_proxy = bus.get_object(GREETER_DBUS_NAME, UNITY_SESSION_DBUS_PATH)
    return dbus.Interface(dbus_proxy, UNITY_SESSION_DBUS_INTERFACE)

GREETER = get_greeter_dbus_interface()


def is_locked():
    """Return bool representing whether screen is locked."""
    return bool(GREETER.get_dbus_method('IsLocked')())


def lock():
    """Lock the screen if its not already locked."""
    if not is_locked():
        GREETER.get_dbus_method('Lock')()


def grab_screenshot():
    """Grab screenshot of the screen and return its content as bytes."""
    with tempfile.NamedTemporaryFile(suffix='.png') as output:
        pyscreenshot.grab_to_file(output.name)
        with open(output.name, 'rb') as file:
            return file.read()
