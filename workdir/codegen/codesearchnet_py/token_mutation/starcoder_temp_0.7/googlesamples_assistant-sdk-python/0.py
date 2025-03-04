def main(record_time, audio_sample_rate, audio_sample_width,
         audio_iter_size, audio_block_size, audio_flush_size):
    """Helper command to test audio samples processing.

    - Record 5 samples of 16-bit during at 16khz.
    - Playback the recorded samples.
    """
    with AudioRecord(record_time,
                     audio_sample_rate,
                     audio_sample_width,
                     audio_iter_size,
                     audio_block_size,
                     audio_flush_size) as rec:
        rec.record()
        rec.play()


