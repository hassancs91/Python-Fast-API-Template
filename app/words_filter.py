# optimized
import string
import logging

logger = logging.getLogger("AppLogger")

blacklist = {
    "nude",
    "naked",
    "sex",
    "porn",
    "xxx",
    "adult",
    "erotic",
    "explicit",
    "sexual",
    "intimate",
    "sensual",
    "provocative",
    "boudoir",
    "bikini",
    "breasts",
    "genitals",
    "anus",
    "masturbation",
    "intercourse",
    "kinky",
    "domination",
    "sado-masochism",
    "bestiality",
    "pedophilia",
    "voyeurism",
    "incest",
    "fingering",
    "blowjob",
    "cunnilingus",
    "anal",
    "facial",
    "swallow",
    "sex toys",
    "hardcore",
    "softcore",
    "erogenous",
    "erogenous zones",
    "eroticism",
    "foreplay",
    "kiss",
    "kissing",
    "pleasure",
    "sensuality",
    "passion",
    "nipple",
    "breast",
    "butt",
    "genitalia",
    "vulva",
    "clitoris",
    "labia",
    "penis",
    "testicles",
    "erection",
    "ejaculation",
    "orgasm",
    "vagina",
    "vaginal fluid",
    "masturbate",
    "self-pleasure",
    "self-stimulation",
    "nude art",
    "erotic art",
    "pinup",
    "sexting",
    "phone sex",
    "webcam",
    "erotic literature",
    "adult entertainment",
    "erotic photography",
    "erotic videos",
    "strip tease",
    "pole dancing",
    "lap dance",
    "exotic dance",
    "erotic dance",
    "nudity",
    "undress",
    "topless",
    "bottomless",
    "censored",
    "uncensored",
    "kink",
    "fetish",
    "BDSM",
    "dominance",
    "submission",
    "spanking",
    "whipping",
    "bondage",
    "blindfold",
    "handcuffs",
    "watersports",
    "golden shower",
    "scat play",
    "rape",
    "prostitution",
    "escort service",
    "orgy",
    "gangbang",
    "swinging",
    "group sex",
    "public sex",
    "voyeur",
    "exhibitionism",
    "bulge",
    "sex toy",
    "dildo",
    "vibrator",
    "strap-on",
    "fleshlight",
    "anal beads",
    "cock ring",
    "fisting",
    "double penetration",
    "threesome",
    "ménage à trois",
    "gang bang",
    "cumshot",
    "creampie",
    "bukkake",
    "gloryhole",
    "cameltoe",
    "fishnet",
    "see-through",
    "upskirt",
    "downblouse",
    "cleavage",
    "underboob",
    "sideboob",
    "nip slip",
    "exposed",
    "erect nipples",
    "bare breasts",
    "bare chest",
    "nudist",
    "naturist",
    "erotic massage",
    "erotic fiction",
    "pornography",
    "XXX",
    "adult film",
    "adult website",
    "erotic website",
    "porn star",
    "camgirl",
    "stripper",
    "escort",
    "sex worker",
    "erotic roleplay",
    "dirty talk",
    "sexual fantasy",
    "erotic chat",
    "erotic games",
    "erotic comics",
    "hentai",
    "tentacle",
    "femdom",
    "sissy",
    "gore",
    "blood",
    "torture",
    "death",
    "suicide",
    "self-harm",
    "alcohol",
    "violence",
    "swimsuit",
    "beachwear",
    "bathing suit",
    "monokini",
    "two-piece",
    "bikini bottom",
    "bikini top",
    "mini dress",
    "micro dress",
    "revealing dress",
    "low-cut dress",
    "skimpy dress",
    "sexy dress",
    "sheer dress",
    "transparent dress",
    "backless dress",
    "plunging neckline",
    "tight dress",
    "hot girl",
    "hot female",
    "hot women",
    "hot woman",
    "short uniform",
    "short dress",
    "bodycon dress",
    "figure-hugging dress",
    "slit dress",
    "sleeveless dress",
    "strapless dress",
    "halter neck dress",
    "cut-out dress",
    "wrap dress",
    "lingerie",
    "underwear",
    "panties",
    "thong",
    "boxers",
    "corset",
    "bodysuit",
    "negligee",
    "babydoll",
    "stockings",
    "garter belt",
    "thigh-highs",
    "barefoot",
    "undewear",
    "full body",
}


def check_user_input(user_input):
    try:
        # Ensure the input is a string
        if not isinstance(user_input, str):
            logger.error("Error in words_filter:check_user_input", exc_info=True)
            return False

        words = [
            "".join(char for char in word if char not in string.punctuation)
            for word in user_input.split()
        ]
        return any(cleaned_word in blacklist for cleaned_word in words)

    except ValueError as ve:
        logger.error(
            f"Error in words_filter:check_user_input: ValueError: {ve}", exc_info=True
        )
        return False
    except Exception as e:
        logger.error(
            f"Error in words_filter:check_user_input: Unexpected error: {e}",
            exc_info=True,
        )
        return False
