from .types import UncleBlock, UncleTemplate


def from_template(template: UncleTemplate) -> UncleBlock:
    return UncleBlock(
        header=template['header'],
        proposals=template['proposals']
    )
