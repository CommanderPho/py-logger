import os
from pushbullet import PushBullet

class PushBulletMixin:
    def init_pushbullet(self, pb_access_token):
        try:
            self.pb = PushBullet(pb_access_token)
            self.pb_enabled = False
        except Exception as e:
            self.e("LOGGER", f"Error in initializing PushBullet, notifications DISABLED: {e}")

    def set_pb_logging_level(self, min_level=-1, levels_list=None):
            if isinstance(min_level, str):
                min_level = self.logging_levels[min_level]
            if min_level > 0:
                self.pb_log_levels = [list(self.logging_levels)[i] for i in range(0, min_level)]
                self.pb_enabled = True
            elif levels_list is not None:
                self.pb_log_levels = levels_list if isinstance(levels_list, list) else [levels_list]
                self.pb_enabled = True
            self.i("LOGGER", f"PushBullet Logging Level Changed: {self.pb_log_levels}")
   
    def toggle_pushbullet(self, enabled):
            self.i("LOGGER", "Logging PUSHBULLET has been " + self.status_string(enabled)+": " + os.path.abspath(self.log_filename))
            self.pb_enabled = enabled