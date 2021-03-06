from django.db import models


class LiveEntryManager(models.Manager):
    def get_query_set(self):
        return super(LiveEntryManager, self).get_query_set()\
            .filter(status__exact=self.model.LIVE_STATUS)
