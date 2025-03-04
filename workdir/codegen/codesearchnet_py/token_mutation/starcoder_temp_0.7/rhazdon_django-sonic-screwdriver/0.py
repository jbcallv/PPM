def handle(self, *args, **options):

        """
        Check, how much time are true.
        If the '--force', '-f' is set this they will be skipped.
        """

        try:
            if options['force']:
                for true_time in TrueTime.objects.all():
                    true_time.skipped = False
                    true_time.save()

            for true_time in TrueTime.objects.all():
                if not true_time.skipped:
                    true_time.check_time()
        except Exception as e:
            print(e)
            return

        self.stdout.write(self.style.SUCCESS("The TrueTime are checked"))

