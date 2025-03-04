def _apply_sub_frames(cls, documents, subs):
        """Convert embedded frames to sub-frames for one or more documents"""
        for doc in documents:
            doc["frames"] = cls._apply_sub_frames_one(doc["frames"], subs)
        return documents

    @classmethod
    def _apply_sub_frames_one(cls, frames, subs):
        """Convert embedded frames to sub-frames for one document"""
        if not subs:
            return frames

        new_frames = []
        for frame in frames:
            if frame["name"] in subs:
                new_frames.append(frame["frames"])
                new_frames.append(subs[frame["name"]])
            else:
                new_frames.append(frame)
        return new_frames

