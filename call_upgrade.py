import os
import upgrade_nijisanji_subscriber as uns
import upgrade_nijisanji_videocount as unv
import upgrade_hololive_subscriber as uhs
import upgrade_hololive_videocount as uhv
import upgrade_vspo_subscriber as uvs
import upgrade_vspo_videocount as uvv
import upgrade_holostars_videocount as uhsv
import upgrade_holostars_subscriber as uhss

def main():
    uhs.main()
    uhv.main()
    uvs.main()
    uvv.main()
    uhss.main()
    uhsv.main()
    uns.main()
    unv.main()


if __name__ == '__main__':
    main()

