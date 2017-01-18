
class CompanyStatus(object):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.name = None  # *(String(50))
        self.defaultFlag = None  # (Boolean)
        self.inactiveFlag = None  # (Boolean)
        self.notifyFlag = None  # (Boolean)
        self.disallowSavingFlag = None  # (Boolean)
        self.notificationMessage = None  # (String(500))
        self.customNoteFlag = None  # (Boolean)
        self.cancelOpenTracksFlag = None  # (Boolean)
        self.track = None  # (TrackReference)
        self._info = None  # (Metadata)

        # initialize object with json dict
        self.__dict__.update(json_dict)

    def __repr__(self):
        string = ''
        for k, v in self.__dict__.items():
            string = ''.join([string, '{}: {}\n'.format(k, v)])
        return string
