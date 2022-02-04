import sys
import time


def typing(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.07)


typing("\n환영합니다, 처음 뵙는 분이네요.")

print()
print()

while True:
    typing("\n당신의 이름은 무엇인가요?")

    print()

    name_insert = input("\n내 이름은..")

    typing(f"\n당신의 이름은 {name_insert}입니까?\n\n1. [예] \n2. [아니오]")

    choice = input("")

    if choice == "1":
        typing(f"\n좋습니다. 기억해둘게요 {name_insert}님.")
        break
    else:
        typing(f"\n제가 잘못들었나봐요. 다시 말씀해주실래요?")
        print()
        continue

print()


flag = False

while True:
    if flag:
        typing(
            f"\n절 다시 찾아왔군요, {name_insert}님. 이제 저와 대화하고 싶으신가요?\n\n1. [응, 뭐가 궁금해?] \n2. [아니, 아직 마음의 준비가 안됐어]"
        )

        choice3 = input(" ")

        if choice3 == "1":
            typing(f"\n다행이에요, {name_insert}님. 그럼 질문을 드릴게요.")
            break
        else:
            typing(f"\n줍으신 분이시군요.. {name_insert}님의 기분이 내킬 때, 다시 찾아와주세요.")
            flag = "0"
            continue

    else:
        typing(
            "\n당신의 성격이 궁금해요.. 우리 좀 더 알아가 볼까요?\n\n1. [좋아, 뭐가 궁금해?] \n2. [음.. 별로 알아가고 싶지 않아]"
        )

        choice2 = input(" ")

        if choice2 == "1":
            typing(f"\n좋아요, {name_insert}님. 그럼 질문을 드릴게요.")
            break
        else:
            typing(
                f"\n아쉽네요..{name_insert}님의 기분이 내킬 때, 다시 찾아와주세요.\n\n1.[다시 대화하고 싶어] \n2.[너랑 더이상 대화하고 싶지 않아]"
            )

            choice4 = input(" ")

            if choice4 == "1":
                pass
            else:
                typing(f"\n그래요... 잘가요, {name_insert}. 언젠간 또 만나길..")
                sys.exit()

            flag = True
            continue


E = False
I = False

print()


while True:
    typing(
        f"\n화이트 크리스마스 이브, {name_insert}님은 친구들과의 술자리에 나가고 싶나요, \n친밀한 소수의 친구들과 시간을 보내고 싶나요? \n\n1. [다함께 즐기는 자리에 빠질 순 없지!] \n2. [따뜻한 분위기에서 조용히 보내고 싶어..]"
    )

    choice3 = input(" ")

    if choice3 == "1":
        typing(f"\n{name_insert}님은 지인들과의 만남으로 스트레스를 해소하는 타입이네요.")
        E = True
        break

    else:
        typing(f"\n{name_insert}님은 좁고 깊은 관계에서 에너지를 충전하는 타입이네요.")
        I = True
        break

EN = False
IN = False
ES = False
IS = False

print()


while E == True:
    typing(
        f"\n덜컹거리는 엘레베이터 안, {name_insert}님은 추락하면 어쩌나 걱정해본 적이 있나요? \n\n1. [당연히 상상해봤지!] \n2. [그런 생각을 왜 해..?]"
    )

    choice5 = input(" ")

    if choice5 == "1":
        typing(f"\n{name_insert}님은 상상력이 풍부한 사람이네요.")
        EN = True
        break

    else:
        typing(f"\n{name_insert}님은 현실적이지 않는 상황에 무관심한 사람이네요.")
        ES = True
        break


while I == True:
    typing(
        f"\n덜컹거리는 엘레베이터 안, {name_insert}님은 추락하면 어쩌나 걱정해본 적이 있나요? \n\n1. [당연히 상상해봤지!] \n2. [그런 생각을 왜 해..?]"
    )

    choice5 = input(" ")

    if choice5 == "1":
        typing(f"\n{name_insert}님은 상상력이 풍부한 사람이네요.")
        IN = True
        break

    else:
        typing(f"\n{name_insert}님은 현실적이지 않는 상황에 무관심한 사람이네요.")
        IS = True
        break


ENT = False
ENF = False
INT = False
INF = False
EST = False
ESF = False
IST = False
ISF = False

print()


while EN == True:
    typing(
        f"\n갑자기 우울해서 화분을 깨트렸다는 친구, {name_insert}님은 어떤 반응인가요? \n\n1. [왜 우울한데 화분을 깨트려?] \n2. [왜 우울해? 무슨 일 있어?]"
    )

    choice6 = input(" ")

    if choice6 == "1":
        typing(f"\n{name_insert}님은 이성적인 사람이네요.")
        ENT = True
        break

    else:
        typing(f"\n{name_insert}님은 감성적인 사람이네요.")
        ENF = False
        break


while ES == True:
    typing(
        f"\n갑자기 우울해서 화분을 깨트렸다는 친구, {name_insert}님은 어떤 반응인가요? \n\n1. [왜 우울한데 화분을 깨트려?] \n2. [왜 우울해? 무슨 일 있어?]"
    )

    choice6 = input(" ")

    if choice6 == "1":
        typing(f"\n{name_insert}님은 이성적인 사람이네요.")
        EST = True
        break

    else:
        typing(f"\n{name_insert}님은 감성적인 사람이네요.")
        ESF = False
        break


while IN == True:
    typing(
        f"\n갑자기 우울해서 화분을 깨트렸다는 친구, {name_insert}님은 어떤 반응인가요? \n\n1. [왜 우울한데 화분을 깨트려?] \n2. [왜 우울해? 무슨 일 있어?]"
    )

    choice6 = input(" ")

    if choice6 == "1":
        typing(f"\n{name_insert}님은 이성적인 사람이네요.")
        INT = True
        break

    else:
        typing(f"\n{name_insert}님은 감성적인 사람이네요.")
        INF = False
        break

while IS == True:
    typing(
        f"\n갑자기 우울해서 화분을 깨트렸다는 친구, {name_insert}님은 어떤 반응인가요? \n\n1. [왜 우울한데 화분을 깨트려?] \n2. [왜 우울해? 무슨 일 있어?]"
    )

    choice6 = input(" ")

    if choice6 == "1":
        typing(f"\n{name_insert}님은 이성적인 사람이네요.")
        IST = True
        break

    else:
        typing(f"\n{name_insert}님은 감성적인 사람이네요.")
        ISF = False
        break


print()


while ENT == True:
    typing(
        f"\n다같이 제주도 여행을 가는 날, {name_insert}님은 어떤 마음가짐인가요? \n\n1. [공항에 도착하면 간단히 식사를 하고 바로 원앙폭포까지 이동해야돼] \n2. [제주도.. 재밌겠다..!]"
    )

    choice7 = input(" ")

    if choice7 == "1":
        typing(f"\n{name_insert}님은 루틴을 지키는 게 편한 계획적인 성향이네요.")
        MBTI = "ENTJ"
        break

    else:
        typing(f"\n{name_insert}님은 즉흥적인 상황을 즐기는 낙관적인 성향이네요.")
        MBTI = "ENTP"
        break


while ENF == True:
    typing(
        f"\n다같이 제주도 여행을 가는 날, {name_insert}님은 어떤 마음가짐인가요? \n\n1. [공항에 도착하면 간단히 식사를 하고 바로 원앙폭포까지 이동해야돼] \n2. [제주도.. 재밌겠다...헿]"
    )

    choice7 = input(" ")

    if choice7 == "1":
        typing(f"\n{name_insert}님은 루틴을 지키는 게 편한 계획적인 성향이네요.")
        MBTI = "ENFJ"
        break

    else:
        typing(f"\n{name_insert}님은 즉흥적인 상황을 즐기는 낙관적인 성향이네요.")
        MBTI = "ENFP"
        break


while EST == True:
    typing(
        f"\n다같이 제주도 여행을 가는 날, {name_insert}님은 어떤 마음가짐인가요? \n\n1. [공항에 도착하면 간단히 식사를 하고 바로 원앙폭포까지 이동해야돼] \n2. [제주도.. 재밌겠다...헿]"
    )

    choice7 = input(" ")

    if choice7 == "1":
        typing(f"\n{name_insert}님은 루틴을 지키는 게 편한 계획적인 성향이네요.")
        MBTI = "ESTJ"
        break

    else:
        typing(f"\n{name_insert}님은 즉흥적인 상황을 즐기는 낙관적인 성향이네요.")
        MBTI = "ESTP"
        break


while ESF == True:
    typing(
        f"\n다같이 제주도 여행을 가는 날, {name_insert}님은 어떤 마음가짐인가요? \n\n1. [공항에 도착하면 간단히 식사를 하고 바로 원앙폭포까지 이동해야돼] \n2. [제주도.. 재밌겠다...헿]"
    )

    choice7 = input(" ")

    if choice7 == "1":
        typing(f"\n{name_insert}님은 루틴을 지키는 게 편한 계획적인 성향이네요.")
        MBTI = "ESFJ"
        break

    else:
        typing(f"\n{name_insert}님은 즉흥적인 상황을 즐기는 낙관적인 성향이네요.")
        MBTI = "ESFP"
        break


while INT == True:
    typing(
        f"\n다같이 제주도 여행을 가는 날, {name_insert}님은 어떤 마음가짐인가요? \n\n1. [공항에 도착하면 간단히 식사를 하고 바로 원앙폭포까지 이동해야돼] \n2. [제주도.. 재밌겠다...헿]"
    )

    choice7 = input(" ")

    if choice7 == "1":
        typing(f"\n{name_insert}님은 루틴을 지키는 게 편한 계획적인 성향이네요.")
        MBTI = "INTJ"
        break

    else:
        typing(f"\n{name_insert}님은 즉흥적인 상황을 즐기는 낙관적인 성향이네요.")
        MBTI = "INTP"
        break


while INF == True:
    typing(
        f"\n다같이 제주도 여행을 가는 날, {name_insert}님은 어떤 마음가짐인가요? \n\n1. [공항에 도착하면 간단히 식사를 하고 바로 원앙폭포까지 이동해야돼] \n2. [제주도.. 재밌겠다...헿]"
    )

    choice7 = input(" ")

    if choice7 == "1":
        typing(f"\n{name_insert}님은 루틴을 지키는 게 편한 계획적인 성향이네요.")
        MBTI = "INFJ"
        break

    else:
        typing(f"\n{name_insert}님은 즉흥적인 상황을 즐기는 낙관적인 성향이네요.")
        MBTI = "INFP"
        break


while IST == True:
    typing(
        f"\n다같이 제주도 여행을 가는 날, {name_insert}님은 어떤 마음가짐인가요? \n\n1. [공항에 도착하면 간단히 식사를 하고 바로 원앙폭포까지 이동해야돼] \n2. [제주도.. 재밌겠다...헿]"
    )

    choice7 = input(" ")

    if choice7 == "1":
        typing(f"\n{name_insert}님은 루틴을 지키는 게 편한 계획적인 성향이네요.")
        MBTI = "ISTJ"
        break

    else:
        typing(f"\n{name_insert}님은 즉흥적인 상황을 즐기는 낙관적인 성향이네요.")
        MBTI = "ISTP"
        break


while ISF == True:
    typing(
        f"\n다같이 제주도 여행을 가는 날, {name_insert}님은 어떤 마음가짐인가요? \n\n1. [공항에 도착하면 간단히 식사를 하고 바로 원앙폭포까지 이동해야돼] \n2. [제주도.. 재밌겠다...헿]"
    )

    choice7 = input(" ")

    if choice7 == "1":
        typing(f"\n{name_insert}님은 루틴을 지키는 게 편한 계획적인 성향이네요.")
        MBTI = "ISFJ"
        break

    else:
        typing(f"\n{name_insert}님은 즉흥적인 상황을 즐기는 낙관적인 성향이네요.")
        MBTI = "ISFP"
        break

print()

typing(f"\n흠....제가 보기엔, {name_insert}님은 {MBTI}일 것 같아요. 맞나요? ")


print()
print()
print()
