from dataclasses import dataclass

@dataclass
class NoteVisibility:
    public = "public"
    home = "home"
    followers = "followers"
    specified = "specified"

@dataclass
class ReactionAcceptance:
    all = None
    likeOnly = "likeOnly"
    likeOnlyForRemote = "likeOnlyForRemote"
    nonSensitiveOnly = "nonSensitiveOnly"
    nonSensitiveOnlyForLocalLikeOnlyForRemote = "nonSensitiveOnlyForLocalLikeOnlyForRemote"