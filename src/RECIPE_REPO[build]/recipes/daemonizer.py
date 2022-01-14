",
      "['[START_DIR]/src/third_party/android_sdk/public/platform-tools/adb', 'devices']",
      "/path/to/tmp/json"
    ],
    "luci_context": {
      "realm": {
        "name": "chromium:ci"
      },
      "resultdb": {
        "current_invocation": {
          "name": "invocations/build:8945511751514863184",
          "update_token": ""
        },
        "hostname": "rdbhost"
      }
    },
    "name": "List adb devices",
    "~followup_annotations": [
      "@@@STEP_LOG_LINE@json.output@[@@@",
      "@@@STEP_LOG_LINE@json.output@  \"014E1F310401C009\"@@@",
      "@@@STEP_LOG_LINE@json.output@]@@@",
      "@@@STEP_LOG_END@json.output@@@"
    ]
  },
  {
    "cmd": [
      "python",
      "-u",
      "\nfrom __future__ import print_function\nimport subprocess\nimport sys\nadb_path = sys.argv[1]\nfor device in sys.argv[2:]:\n  print('Attempting to root device %s ...' % device)\n  subprocess.check_call([adb_path, '-s', device, 'root'])\n  subprocess.check_call([adb_path, '-s', device, 'wait-for-device'])\n  print('Finished rooting device %s' % device)\n",
      "[START_DIR]/src/third_party/android_sdk/public/platform-tools/adb",
      "014E1F310401C009"
    ],
    "luci_context": {
      "realm": {
        "name": "chromium:ci"
      },
      "resultdb": {
        "current_invocation": {
          "name": "invocations/build:8945511751514863184",
          "update_token": "token"
        },
        "hostname": "rdbhost"
      }
    },
    "name": "Root devices",
    "~followup_annotations": [
      "@@@STEP_LOG_LINE@python.inline@@@@",
      "@@@STEP_LOG_LINE@python.inline@from __future__ import print_function@@@",
      "@@@STEP_LOG_LINE@python.inline@import subprocess@@@",
      "@@@STEP_LOG_LINE@python.inline@import sys@@@",
      "@@@STEP_LOG_LINE@python.inline@adb_path = sys.argv[1]@@@",
      "@@@STEP_LOG_LINE@python.inline@for device in sys.argv[2:]:@@@",
      "@@@STEP_LOG_LINE@python.inline@  print('Attempting to root device %s ...' % device)@@@",
      "@@@STEP_LOG_LINE@python.inline@  subprocess.check_call([adb_path, '-s', device, 'root'])@@@",
      "@@@STEP_LOG_LINE@python.inline@  subprocess.check_call([adb_path, '-s', device, 'wait-for-device'])@@@",
      "@@@STEP_LOG_LINE@python.inline@  print('Finished rooting device %s' % device)@@@",
      "@@@STEP_LOG_END@python.inline@@@"
    ]
  },
  {
    "cmd": [
      "python",
      "-u",
      "RECIPE_REPO[build]/scripts/tools/runit.py",
      "--show-path",
      "--with-third-party-lib",
      "--",
      "python",
      "RECIPE_REPO[build]/recipes/daemonizer.py",
      "--",
      "[START_DIR]/src/build/android/adb_logcat_monitor.py",
      "[START_DIR]/src/out/logcat",
      "[START_DIR]/src/third_party/android_sdk/public/platform-tools/adb"
    ],
    "env": {
      "PATH": "[START_DIR]/src/third_party/android_sdk/public/platform-tools:[START_DIR]/src/build/android:<PATH>"
    },
    "infra_step": true,
    "luci_context": {
      "realm": {
        "name": "chromium:ci"
      },
      "resultdb": {
        "current_invocation": {
          "name": "invocations/build:8945511751514863184",
          "update_token": "token"
        },
        "hostname": "rdbhost"
      }
    },
    "name": "spawn_logcat_monitor"
  },
  {
    "cmd": [
      "vpython",
      "-u",
      "[START_DIR]/src/third_party/catapult/devil/devil/android/tools/device_recovery.py",
      "--denylist-file",
      "[START_DIR]/src/out/bad_devices.json",
      "--known-devices-file",
      "[HOME]/.android.json",
      "--adb-path",
      "[START_DIR]/src/console.cloud.google.com/home/dashboard?project=bootdisk&_ga=2.208140629.61701763.1642051256-1894524119.1641455309
