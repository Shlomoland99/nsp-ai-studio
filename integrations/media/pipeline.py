from dataclasses import dataclass
@dataclass(frozen=True)
class MediaArtifact: path:str; media_type:str; checksum:str|None=None
class ProductionMediaPipeline:
    def validate(self,artifact:MediaArtifact)->MediaArtifact:
        if not artifact.path: raise ValueError("Artifact path is required")
        return artifact