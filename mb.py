from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("キャラクターのレアリティ")]
# [Flags]
class CharacterRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("N")]
    N = 1
    # [Description("R")]
    R = 2
    # [Description("R+")]
    RPlus = 4
    # [Description("SR")]
    SR = 8
    # [Description("SR+")]
    SRPlus = 16
    # [Description("SSR")]
    SSR = 32
    # [Description("SSR+")]
    SSRPlus = 64
    # [Description("UR")]
    UR = 128
    # [Description("UR+")]
    URPlus = 256
    # [Description("LR")]
    LR = 512
    # [Description("LR+")]
    LRPlus = 1024
    # [Description("LR+2")]
    LRPlus2 = 2048
    # [Description("LR+3")]
    LRPlus3 = 4096
    # [Description("LR+4")]
    LRPlus4 = 8192
    # [Description("LR+5")]
    LRPlus5 = 16384
    # [Description("LR+6")]
    LRPlus6 = 32768
    # [Description("LR+7")]
    LRPlus7 = 65536

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [Description("パッシブスキルトリガー")]
class PassiveTrigger(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("ターン開始時")]
    TurnStart = 1
    # [Description("ターン終了時")]
    TurnEnd = 2
    # [Description("計算前パッシブ")]
    BeforeCalculation = 3
    # [Description("被致命的ダメージ時")]
    InstantDeathDamage = 5
    # [Description("自分死亡時")]
    SelfDead = 6
    # [Description("第三者味方死亡時")]
    AllyDead = 7
    # [Description("被攻撃時")]
    ReceiveDamage = 8
    # [Description("攻撃時")]
    GiveDamage = 9
    # [Description("第三者の攻撃時、味方の被攻撃時")]
    AllyReceiveDamage = 10
    # [Description("被デバフ時")]
    ReceiveDebuff = 11
    # [Description("デバフ時")]
    GiveDeBuff = 12
    # [Description("第三者のデバフ時")]
    AllyReceiveDeBuff = 13
    # [Description("回復時")]
    GiveHeal = 14
    # [Description("第三者の回復時")]
    AllyReceiveHeal = 15
    # [Description("バフ時")]
    GiveBuff = 16
    # [Description("第三者のバフ時")]
    AllyGiveBuff = 17
    # [Description("敵復活時")]
    EnemyRecovery = 18
    # [Description("自分復活時")]
    SelfRecovery = 19
    # [Description("第三者敵死亡時パッシブ")]
    OtherEnemyDead = 20
    # [Description("敵死亡時")]
    EnemyDead = 21
    # [Description("第三者味方の攻撃時")]
    AllyGiveDamage = 22
    # [Description("第三者敵の与回復時")]
    EnemyReceiveHeal = 23
    # [Description("被バフ時")]
    ReceiveBuff = 24
    # [Description("第三者敵のバフ時")]
    EnemyGiveBuff = 25
    # [Description("戦闘開始時")]
    BattleStart = 26
    # [Description("戦闘終了時")]
    BattleEnd = 27
    # [Description("ターン開始時(行動順決定前)")]
    TurnStartBeforeSpeedCheck = 28
    # [Description("被攻撃時（命中or回避）")]
    TargetAttack = 29
    # [Description("被ダメージ量判定(自分の情報だけ参照)")]
    CheckReceiveDamageSelf = 41
    # [Description("被ダメージ量判定")]
    CheckReceiveDamage = 42

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("パラメーター増減タイプ")]
class ChangeParameterType(Enum):
    # [Description("加算(+X)")]
    Addition = 1
    # [Description("乗算(+X%)")]
    AdditionPercent = 2
    # [Description("キャラLv×係数")]
    CharacterLevelConstantMultiplicationAddition = 3

# [Description("バトルパラメータの種類")]
class BattleParameterType(Enum):
    # [Description("HP")]
    Hp = 1
    # [Description("攻撃力")]
    AttackPower = 2
    # [Description("物理ダメージ緩和")]
    PhysicalDamageRelax = 3
    # [Description("魔法ダメージ緩和")]
    MagicDamageRelax = 4
    # [Description("命中")]
    Hit = 5
    # [Description("回避")]
    Avoidance = 6
    # [Description("クリティカル")]
    Critical = 7
    # [Description("クリティカル耐性")]
    CriticalResist = 8
    # [Description("クリダメ強化")]
    CriticalDamageEnhance = 9
    # [Description("物理クリダメ緩和")]
    PhysicalCriticalDamageRelax = 10
    # [Description("魔法クリダメ緩和")]
    MagicCriticalDamageRelax = 11
    # [Description("防御貫通力")]
    DefensePenetration = 12
    # [Description("防御力")]
    Defense = 13
    # [Description("物魔防御貫通")]
    DamageEnhance = 14
    # [Description("弱体効果命中")]
    DebuffHit = 15
    # [Description("弱体効果耐性")]
    DebuffResist = 16
    # [Description("リフレクト")]
    DamageReflect = 17
    # [Description("HP吸収")]
    HpDrain = 18
    # [Description("スピード")]
    Speed = 19

# [Description("パラメーター増減タイプ")]
class ChangeParameterType(Enum):
    # [Description("加算(+X)")]
    Addition = 1
    # [Description("乗算(+X%)")]
    AdditionPercent = 2
    # [Description("キャラLv×係数")]
    CharacterLevelConstantMultiplicationAddition = 3

# [Description("基礎パラメータの種類")]
class BaseParameterType(Enum):
    # [Description("筋力")]
    Muscle = 1
    # [Description("技力")]
    Energy = 2
    # [Description("魔力")]
    Intelligence = 3
    # [Description("耐久力")]
    Health = 4

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("神器タイプ")]
class SacredTreasureType(Enum):
    # [Description("神器ではない")]
    None_ = 0
    # [Description("魔装")]
    Matchless = 1
    # [Description("聖装")]
    Legend = 2
    # [Description("双ステータス神器")]
    DualStatus = 3

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [Description("神器タイプ")]
class SacredTreasureType(Enum):
    # [Description("神器ではない")]
    None_ = 0
    # [Description("魔装")]
    Matchless = 1
    # [Description("聖装")]
    Legend = 2
    # [Description("双ステータス神器")]
    DualStatus = 3

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [MessagePackObject(True)]
@dataclass
class CustomTextLayoutInfo():
    BannerAlignment: int
    BannerFontSize: int
    BannerLetterSpacing: float
    BannerLineSpacing: float
    BannerOutlineColor: str
    BannerPositionX: float
    BannerPositionY: float
    TitleFontSize: int

# [MessagePackObject(True)]
@dataclass
class CustomTextLayoutInfo():
    BannerAlignment: int
    BannerFontSize: int
    BannerLetterSpacing: float
    BannerLineSpacing: float
    BannerOutlineColor: str
    BannerPositionX: float
    BannerPositionY: float
    TitleFontSize: int

# [MessagePackObject(True)]
@dataclass
class CustomTextLayoutInfo():
    BannerAlignment: int
    BannerFontSize: int
    BannerLetterSpacing: float
    BannerLineSpacing: float
    BannerOutlineColor: str
    BannerPositionX: float
    BannerPositionY: float
    TitleFontSize: int

# [MessagePackObject(True)]
@dataclass
class CustomTextLayoutInfo():
    BannerAlignment: int
    BannerFontSize: int
    BannerLetterSpacing: float
    BannerLineSpacing: float
    BannerOutlineColor: str
    BannerPositionX: float
    BannerPositionY: float
    TitleFontSize: int

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("キャラクターのレアリティ")]
# [Flags]
class CharacterRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("N")]
    N = 1
    # [Description("R")]
    R = 2
    # [Description("R+")]
    RPlus = 4
    # [Description("SR")]
    SR = 8
    # [Description("SR+")]
    SRPlus = 16
    # [Description("SSR")]
    SSR = 32
    # [Description("SSR+")]
    SSRPlus = 64
    # [Description("UR")]
    UR = 128
    # [Description("UR+")]
    URPlus = 256
    # [Description("LR")]
    LR = 512
    # [Description("LR+")]
    LRPlus = 1024
    # [Description("LR+2")]
    LRPlus2 = 2048
    # [Description("LR+3")]
    LRPlus3 = 4096
    # [Description("LR+4")]
    LRPlus4 = 8192
    # [Description("LR+5")]
    LRPlus5 = 16384
    # [Description("LR+6")]
    LRPlus6 = 32768
    # [Description("LR+7")]
    LRPlus7 = 65536

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [Description("キャラクターのレアリティ")]
# [Flags]
class CharacterRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("N")]
    N = 1
    # [Description("R")]
    R = 2
    # [Description("R+")]
    RPlus = 4
    # [Description("SR")]
    SR = 8
    # [Description("SR+")]
    SRPlus = 16
    # [Description("SSR")]
    SSR = 32
    # [Description("SSR+")]
    SSRPlus = 64
    # [Description("UR")]
    UR = 128
    # [Description("UR+")]
    URPlus = 256
    # [Description("LR")]
    LR = 512
    # [Description("LR+")]
    LRPlus = 1024
    # [Description("LR+2")]
    LRPlus2 = 2048
    # [Description("LR+3")]
    LRPlus3 = 4096
    # [Description("LR+4")]
    LRPlus4 = 8192
    # [Description("LR+5")]
    LRPlus5 = 16384
    # [Description("LR+6")]
    LRPlus6 = 32768
    # [Description("LR+7")]
    LRPlus7 = 65536

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [MessagePackObject(True)]
@dataclass
class MissionReward():
    # [Nest(True, 1)]
    # [PropertyOrder(1)]
    Item: UserItem
    # [PropertyOrder(2)]
    RarityFlags: CharacterRarityFlags

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("パラメーター増減タイプ")]
class ChangeParameterType(Enum):
    # [Description("加算(+X)")]
    Addition = 1
    # [Description("乗算(+X%)")]
    AdditionPercent = 2
    # [Description("キャラLv×係数")]
    CharacterLevelConstantMultiplicationAddition = 3

# [Description("バトルパラメータの種類")]
class BattleParameterType(Enum):
    # [Description("HP")]
    Hp = 1
    # [Description("攻撃力")]
    AttackPower = 2
    # [Description("物理ダメージ緩和")]
    PhysicalDamageRelax = 3
    # [Description("魔法ダメージ緩和")]
    MagicDamageRelax = 4
    # [Description("命中")]
    Hit = 5
    # [Description("回避")]
    Avoidance = 6
    # [Description("クリティカル")]
    Critical = 7
    # [Description("クリティカル耐性")]
    CriticalResist = 8
    # [Description("クリダメ強化")]
    CriticalDamageEnhance = 9
    # [Description("物理クリダメ緩和")]
    PhysicalCriticalDamageRelax = 10
    # [Description("魔法クリダメ緩和")]
    MagicCriticalDamageRelax = 11
    # [Description("防御貫通力")]
    DefensePenetration = 12
    # [Description("防御力")]
    Defense = 13
    # [Description("物魔防御貫通")]
    DamageEnhance = 14
    # [Description("弱体効果命中")]
    DebuffHit = 15
    # [Description("弱体効果耐性")]
    DebuffResist = 16
    # [Description("リフレクト")]
    DamageReflect = 17
    # [Description("HP吸収")]
    HpDrain = 18
    # [Description("スピード")]
    Speed = 19

# [Description("パラメーター増減タイプ")]
class ChangeParameterType(Enum):
    # [Description("加算(+X)")]
    Addition = 1
    # [Description("乗算(+X%)")]
    AdditionPercent = 2
    # [Description("キャラLv×係数")]
    CharacterLevelConstantMultiplicationAddition = 3

# [Description("基礎パラメータの種類")]
class BaseParameterType(Enum):
    # [Description("筋力")]
    Muscle = 1
    # [Description("技力")]
    Energy = 2
    # [Description("魔力")]
    Intelligence = 3
    # [Description("耐久力")]
    Health = 4

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [MessagePackObject(True)]
@dataclass
class PassiveSubSetSkillInfo():
    # [Description("パッシブトリガー")]
    PassiveTrigger: PassiveTrigger
    # [Description("スキルクールタイム(MB : 初期スキルクールタイム)")]
    SkillCoolTime: int
    # [Description("スキルMAXクールタイム")]
    SkillMaxCoolTime: int
    # [Description("サブセットスキルId")]
    SubSetSkillId: int

# [Description("武具のレアリティ")]
# [Flags]
class EquipmentRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("D")]
    D = 1
    # [Description("C")]
    C = 2
    # [Description("B")]
    B = 4
    # [Description("A")]
    A = 8
    # [Description("S")]
    S = 16
    # [Description("R")]
    R = 32
    # [Description("SR")]
    SR = 64
    # [Description("SSR")]
    SSR = 128
    # [Description("UR")]
    UR = 256
    # [Description("LR")]
    LR = 512

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [Description("キャラクターのレアリティ")]
# [Flags]
class CharacterRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("N")]
    N = 1
    # [Description("R")]
    R = 2
    # [Description("R+")]
    RPlus = 4
    # [Description("SR")]
    SR = 8
    # [Description("SR+")]
    SRPlus = 16
    # [Description("SSR")]
    SSR = 32
    # [Description("SSR+")]
    SSRPlus = 64
    # [Description("UR")]
    UR = 128
    # [Description("UR+")]
    URPlus = 256
    # [Description("LR")]
    LR = 512
    # [Description("LR+")]
    LRPlus = 1024
    # [Description("LR+2")]
    LRPlus2 = 2048
    # [Description("LR+3")]
    LRPlus3 = 4096
    # [Description("LR+4")]
    LRPlus4 = 8192
    # [Description("LR+5")]
    LRPlus5 = 16384
    # [Description("LR+6")]
    LRPlus6 = 32768
    # [Description("LR+7")]
    LRPlus7 = 65536

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [Description("キャラクターのレアリティ")]
# [Flags]
class CharacterRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("N")]
    N = 1
    # [Description("R")]
    R = 2
    # [Description("R+")]
    RPlus = 4
    # [Description("SR")]
    SR = 8
    # [Description("SR+")]
    SRPlus = 16
    # [Description("SSR")]
    SSR = 32
    # [Description("SSR+")]
    SSRPlus = 64
    # [Description("UR")]
    UR = 128
    # [Description("UR+")]
    URPlus = 256
    # [Description("LR")]
    LR = 512
    # [Description("LR+")]
    LRPlus = 1024
    # [Description("LR+2")]
    LRPlus2 = 2048
    # [Description("LR+3")]
    LRPlus3 = 4096
    # [Description("LR+4")]
    LRPlus4 = 8192
    # [Description("LR+5")]
    LRPlus5 = 16384
    # [Description("LR+6")]
    LRPlus6 = 32768
    # [Description("LR+7")]
    LRPlus7 = 65536

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [MessagePackObject(True)]
@dataclass
class LocalRaidQuestIdWeight():
    # [Description("幻影の神殿のクエストId")]
    # [PropertyOrder(1)]
    LocalRaidQuestId: int
    # [Description("出現割合")]
    # [PropertyOrder(2)]
    LotteryWeight: int

class LocalRaidQuestGroupType(Enum):
    # [Description("1欄")]
    First = 1
    # [Description("2欄")]
    Second = 2
    # [Description("3欄")]
    Third = 3
    # [Description("4欄")]
    Fourth = 4
    # [Description("5欄")]
    Fifth = 5

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("キャラクターのレアリティ")]
# [Flags]
class CharacterRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("N")]
    N = 1
    # [Description("R")]
    R = 2
    # [Description("R+")]
    RPlus = 4
    # [Description("SR")]
    SR = 8
    # [Description("SR+")]
    SRPlus = 16
    # [Description("SSR")]
    SSR = 32
    # [Description("SSR+")]
    SSRPlus = 64
    # [Description("UR")]
    UR = 128
    # [Description("UR+")]
    URPlus = 256
    # [Description("LR")]
    LR = 512
    # [Description("LR+")]
    LRPlus = 1024
    # [Description("LR+2")]
    LRPlus2 = 2048
    # [Description("LR+3")]
    LRPlus3 = 4096
    # [Description("LR+4")]
    LRPlus4 = 8192
    # [Description("LR+5")]
    LRPlus5 = 16384
    # [Description("LR+6")]
    LRPlus6 = 32768
    # [Description("LR+7")]
    LRPlus7 = 65536

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [Description("キャラクターのレアリティ")]
# [Flags]
class CharacterRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("N")]
    N = 1
    # [Description("R")]
    R = 2
    # [Description("R+")]
    RPlus = 4
    # [Description("SR")]
    SR = 8
    # [Description("SR+")]
    SRPlus = 16
    # [Description("SSR")]
    SSR = 32
    # [Description("SSR+")]
    SSRPlus = 64
    # [Description("UR")]
    UR = 128
    # [Description("UR+")]
    URPlus = 256
    # [Description("LR")]
    LR = 512
    # [Description("LR+")]
    LRPlus = 1024
    # [Description("LR+2")]
    LRPlus2 = 2048
    # [Description("LR+3")]
    LRPlus3 = 4096
    # [Description("LR+4")]
    LRPlus4 = 8192
    # [Description("LR+5")]
    LRPlus5 = 16384
    # [Description("LR+6")]
    LRPlus6 = 32768
    # [Description("LR+7")]
    LRPlus7 = 65536

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [Description("キャラクターのレアリティ")]
# [Flags]
class CharacterRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("N")]
    N = 1
    # [Description("R")]
    R = 2
    # [Description("R+")]
    RPlus = 4
    # [Description("SR")]
    SR = 8
    # [Description("SR+")]
    SRPlus = 16
    # [Description("SSR")]
    SSR = 32
    # [Description("SSR+")]
    SSRPlus = 64
    # [Description("UR")]
    UR = 128
    # [Description("UR+")]
    URPlus = 256
    # [Description("LR")]
    LR = 512
    # [Description("LR+")]
    LRPlus = 1024
    # [Description("LR+2")]
    LRPlus2 = 2048
    # [Description("LR+3")]
    LRPlus3 = 4096
    # [Description("LR+4")]
    LRPlus4 = 8192
    # [Description("LR+5")]
    LRPlus5 = 16384
    # [Description("LR+6")]
    LRPlus6 = 32768
    # [Description("LR+7")]
    LRPlus7 = 65536

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("ヘルプ付加情報タイプ")]
class HelpParameterType(Enum):
    # [Description("無し")]
    None_ = 0
    # [Description("所属するワールド")]
    BelongingWorlds = 1

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [MessagePackObject(True)]
@dataclass
class GuildRaidGoldCoefficientInfo():
    AdditiveCoefficient: int
    DivisionCoefficient: int

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [MessagePackObject(True)]
@dataclass
class CustomTextLayoutInfo():
    BannerAlignment: int
    BannerFontSize: int
    BannerLetterSpacing: float
    BannerLineSpacing: float
    BannerOutlineColor: str
    BannerPositionX: float
    BannerPositionY: float
    TitleFontSize: int

# [MessagePackObject(True)]
@dataclass
class CustomTextLayoutInfo():
    BannerAlignment: int
    BannerFontSize: int
    BannerLetterSpacing: float
    BannerLineSpacing: float
    BannerOutlineColor: str
    BannerPositionX: float
    BannerPositionY: float
    TitleFontSize: int

# [MessagePackObject(True)]
@dataclass
class CustomTextLayoutInfo():
    BannerAlignment: int
    BannerFontSize: int
    BannerLetterSpacing: float
    BannerLineSpacing: float
    BannerOutlineColor: str
    BannerPositionX: float
    BannerPositionY: float
    TitleFontSize: int

# [MessagePackObject(True)]
@dataclass
class CustomTextLayoutInfo():
    BannerAlignment: int
    BannerFontSize: int
    BannerLetterSpacing: float
    BannerLineSpacing: float
    BannerOutlineColor: str
    BannerPositionX: float
    BannerPositionY: float
    TitleFontSize: int

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("バトルパラメータ変動情報")]
# [MessagePackObject(True)]
@dataclass
class BattleParameterChangeInfo():
    # [Description("変動するバトルパラメータ")]
    # [PropertyOrder(1)]
    BattleParameterType: BattleParameterType
    # [Description("パラメータ増減タイプ")]
    # [PropertyOrder(2)]
    ChangeParameterType: ChangeParameterType
    # [Description("値")]
    # [PropertyOrder(3)]
    Value: float

# [Description("基礎パラメータ変動情報")]
# [MessagePackObject(True)]
@dataclass
class BaseParameterChangeInfo():
    # [Description("変動する基礎パラメータ")]
    # [PropertyOrder(1)]
    BaseParameterType: BaseParameterType
    # [Description("パラメータ増減タイプ")]
    # [PropertyOrder(2)]
    ChangeParameterType: ChangeParameterType
    # [Description("値")]
    # [PropertyOrder(3)]
    Value: float

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [Description("パラメーター増減タイプ")]
class ChangeParameterType(Enum):
    # [Description("加算(+X)")]
    Addition = 1
    # [Description("乗算(+X%)")]
    AdditionPercent = 2
    # [Description("キャラLv×係数")]
    CharacterLevelConstantMultiplicationAddition = 3

# [Description("バトルパラメータの種類")]
class BattleParameterType(Enum):
    # [Description("HP")]
    Hp = 1
    # [Description("攻撃力")]
    AttackPower = 2
    # [Description("物理ダメージ緩和")]
    PhysicalDamageRelax = 3
    # [Description("魔法ダメージ緩和")]
    MagicDamageRelax = 4
    # [Description("命中")]
    Hit = 5
    # [Description("回避")]
    Avoidance = 6
    # [Description("クリティカル")]
    Critical = 7
    # [Description("クリティカル耐性")]
    CriticalResist = 8
    # [Description("クリダメ強化")]
    CriticalDamageEnhance = 9
    # [Description("物理クリダメ緩和")]
    PhysicalCriticalDamageRelax = 10
    # [Description("魔法クリダメ緩和")]
    MagicCriticalDamageRelax = 11
    # [Description("防御貫通力")]
    DefensePenetration = 12
    # [Description("防御力")]
    Defense = 13
    # [Description("物魔防御貫通")]
    DamageEnhance = 14
    # [Description("弱体効果命中")]
    DebuffHit = 15
    # [Description("弱体効果耐性")]
    DebuffResist = 16
    # [Description("リフレクト")]
    DamageReflect = 17
    # [Description("HP吸収")]
    HpDrain = 18
    # [Description("スピード")]
    Speed = 19

# [Description("パラメーター増減タイプ")]
class ChangeParameterType(Enum):
    # [Description("加算(+X)")]
    Addition = 1
    # [Description("乗算(+X%)")]
    AdditionPercent = 2
    # [Description("キャラLv×係数")]
    CharacterLevelConstantMultiplicationAddition = 3

# [Description("バトルパラメータの種類")]
class BattleParameterType(Enum):
    # [Description("HP")]
    Hp = 1
    # [Description("攻撃力")]
    AttackPower = 2
    # [Description("物理ダメージ緩和")]
    PhysicalDamageRelax = 3
    # [Description("魔法ダメージ緩和")]
    MagicDamageRelax = 4
    # [Description("命中")]
    Hit = 5
    # [Description("回避")]
    Avoidance = 6
    # [Description("クリティカル")]
    Critical = 7
    # [Description("クリティカル耐性")]
    CriticalResist = 8
    # [Description("クリダメ強化")]
    CriticalDamageEnhance = 9
    # [Description("物理クリダメ緩和")]
    PhysicalCriticalDamageRelax = 10
    # [Description("魔法クリダメ緩和")]
    MagicCriticalDamageRelax = 11
    # [Description("防御貫通力")]
    DefensePenetration = 12
    # [Description("防御力")]
    Defense = 13
    # [Description("物魔防御貫通")]
    DamageEnhance = 14
    # [Description("弱体効果命中")]
    DebuffHit = 15
    # [Description("弱体効果耐性")]
    DebuffResist = 16
    # [Description("リフレクト")]
    DamageReflect = 17
    # [Description("HP吸収")]
    HpDrain = 18
    # [Description("スピード")]
    Speed = 19

# [Description("パラメーター増減タイプ")]
class ChangeParameterType(Enum):
    # [Description("加算(+X)")]
    Addition = 1
    # [Description("乗算(+X%)")]
    AdditionPercent = 2
    # [Description("キャラLv×係数")]
    CharacterLevelConstantMultiplicationAddition = 3

# [Description("基礎パラメータの種類")]
class BaseParameterType(Enum):
    # [Description("筋力")]
    Muscle = 1
    # [Description("技力")]
    Energy = 2
    # [Description("魔力")]
    Intelligence = 3
    # [Description("耐久力")]
    Health = 4

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [Description("武具のレアリティ")]
# [Flags]
class EquipmentRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("D")]
    D = 1
    # [Description("C")]
    C = 2
    # [Description("B")]
    B = 4
    # [Description("A")]
    A = 8
    # [Description("S")]
    S = 16
    # [Description("R")]
    R = 32
    # [Description("SR")]
    SR = 64
    # [Description("SSR")]
    SSR = 128
    # [Description("UR")]
    UR = 256
    # [Description("LR")]
    LR = 512

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("パラメーター増減タイプ")]
class ChangeParameterType(Enum):
    # [Description("加算(+X)")]
    Addition = 1
    # [Description("乗算(+X%)")]
    AdditionPercent = 2
    # [Description("キャラLv×係数")]
    CharacterLevelConstantMultiplicationAddition = 3

# [Description("バトルパラメータの種類")]
class BattleParameterType(Enum):
    # [Description("HP")]
    Hp = 1
    # [Description("攻撃力")]
    AttackPower = 2
    # [Description("物理ダメージ緩和")]
    PhysicalDamageRelax = 3
    # [Description("魔法ダメージ緩和")]
    MagicDamageRelax = 4
    # [Description("命中")]
    Hit = 5
    # [Description("回避")]
    Avoidance = 6
    # [Description("クリティカル")]
    Critical = 7
    # [Description("クリティカル耐性")]
    CriticalResist = 8
    # [Description("クリダメ強化")]
    CriticalDamageEnhance = 9
    # [Description("物理クリダメ緩和")]
    PhysicalCriticalDamageRelax = 10
    # [Description("魔法クリダメ緩和")]
    MagicCriticalDamageRelax = 11
    # [Description("防御貫通力")]
    DefensePenetration = 12
    # [Description("防御力")]
    Defense = 13
    # [Description("物魔防御貫通")]
    DamageEnhance = 14
    # [Description("弱体効果命中")]
    DebuffHit = 15
    # [Description("弱体効果耐性")]
    DebuffResist = 16
    # [Description("リフレクト")]
    DamageReflect = 17
    # [Description("HP吸収")]
    HpDrain = 18
    # [Description("スピード")]
    Speed = 19

# [Description("パッシブスキル種別")]
class PassiveType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("キャラパッシブタイプ")]
    EachUnit = 1
    # [Description("チームパッシブタイプ")]
    Team = 2

# [Description("遷移先タイプ")]
class TransferSpotType(Enum):
    # [Description("遷移無し")]
    None_ = 0
    # [Description("放置バトル")]
    AutoBattle = 10
    # [Description("祈りの泉")]
    BountyQuest = 20
    # [Description("時空の洞窟")]
    DungeonBattle = 30
    # [Description("ガチャ")]
    GachaCase = 40
    # [Description("試練")]
    Competition = 50
    # [Description("幻影の神殿")]
    LocalRaid = 60
    # [Description("お知らせ")]
    Notice = 70
    # [Description("ロイヤルショップ（タブ指定）")]
    ShopTab = 80
    # [Description("ロイヤルショップ（商品指定）")]
    ShopItem = 81
    # [Description("無窮の塔（通常）")]
    TowerBattle = 90
    # [Description("無窮の塔（塔指定）")]
    TowerBattleSelectTower = 91
    # [Description("交換所")]
    TradeShop = 100
    # [Description("外部ウェブサイト")]
    OuterWebSite = 110
    # [Description("月間ログインボーナス")]
    MonthlyLoginBonus = 120
    # [Description("期間限定ログインボーナス")]
    LimitedLoginBonus = 121
    # [Description("初心者ミッション")]
    BeginnerMission = 130
    # [Description("カムバックミッション")]
    ComebackMission = 131
    # [Description("新キャラミッション")]
    NewCharacterMission = 132
    # [Description("イベントミッション")]
    EventMission = 133
    # [Description("友達招待")]
    FriendCampaign = 134
    # [Description("ゲリラパック")]
    GuerrillaPack = 140
    # [Description("格納アイコン")]
    StoreIcon = 150
    # [Description("キャラ")]
    Character = 160
    # [Description("チャット")]
    Chat = 170
    # [Description("ギルド")]
    Guild = 180
    # [Description("ギルドレイド")]
    GuildRaid = 181
    # [Description("ギルドレイドワールドダメージ報酬ダイアログ")]
    GuildRaidWorldReward = 182
    # [Description("フレンド")]
    Friend = 4

# [Description("ミッション達成条件タイプ")]
class MissionAchievementType(Enum):
    # [Description("無し")]
    None_ = 0
    # [Description("日付をまたいでログインした時")]
    Login = 100
    # [Description("ダイヤによる購入")]
    BoughtByCurrency = 200
    # [Description("フレンドコード使用")]
    UseFriendCode = 300
    # [Description("新キャラミッション")]
    NewCharacter = 1000
    # [Description("カムバックミッション中に貢献メダルを獲得した時")]
    MissionTotalActivityAtComeback = 1010100
    # [Description("新キャラミッション中に貢献メダルを獲得した時")]
    MissionTotalActivityAtNewCharacterMission = 1010200
    # [Description("期間限定ミッション中に貢献メダルを獲得した時")]
    MissionTotalActivityAtEvent = 1010300
    # [Description("マイページで自己紹介文を変更した時")]
    PlayerInfoEditComment = 2010100
    # [Description("フレンドになった最大の人数")]
    FriendMaxFriendCount = 3010100
    # [Description("フレンドポイントを送信した時")]
    FriendSendFriendPointCount = 3010200
    # [Description("アカウント連携を行った時")]
    SocialAuthAccount = 4010100
    # [Description("公式Twitterフォロー")]
    SocialFollowOfficialTwitter = 4020100
    # [Description("公式Youtubeフォロー")]
    SocialFollowOfficialYoutube = 4020200
    # [Description("ショップ（聖装鋼タブ）購入回数")]
    ExchangeLegendForgeMergeCount = 5010100
    # [Description("ショップ（精錬鋼タブ）購入回数")]
    ExchangeEquipmentForgeMergeCount = 5020200
    # [Description("ショップ（全てのタブ）購入回数")]
    ExchangeAllBuyCount = 5030100
    # [Description("ショップ（レギュラータブ）購入回数")]
    ExchangeRegularBuyCount = 5030200
    # [Description("ショップ（ギルドタブ）購入回数")]
    ExchangeGvGBuyCount = 5040100
    # [Description("ショップ（時空の洞窟タブ）購入回数")]
    ExchangeDungeonBattleBuyCount = 5050100
    # [Description("ロイヤルショップのダイヤ購入でダイヤを購入した時")]
    ShopTotalBuyCurrency = 6010100
    # [Description("キャラレベルアップ")]
    CharacterLevelUpCount = 7010100
    # [Description("レベルリンク達成レベル")]
    CharacterLevelLinkMaxLevel = 7010200
    # [Description("武具達成レベル")]
    CharacterEquipmentMaxLevel = 7010300
    # [Description("Lv1スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel1 = 7010401
    # [Description("Lv2スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel2 = 7010402
    # [Description("Lv3スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel3 = 7010403
    # [Description("Lv4スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel4 = 7010404
    # [Description("Lv5スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel5 = 7010405
    # [Description("Lv6スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel6 = 7010406
    # [Description("Lv7スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel7 = 7010407
    # [Description("Lv8スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel8 = 7010408
    # [Description("Lv9スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel9 = 7010409
    # [Description("魔装達成レベル")]
    CharacterMatchlessSacredTreasureMaxLevel = 7010500
    # [Description("聖装達成レベル")]
    CharacterLegendSacredTreasureMaxLevel = 7010600
    # [Description("武具研磨回数")]
    CharacterEquipmentTrainingCount = 7010700
    # [Description("武具強化達成レベル")]
    CharacterEquipmentReinforceMaxLevel = 7010800
    # [Description("神装強化回数")]
    CharacterEquipmentMergeCount = 7010900
    # [Description("最大総戦闘力")]
    CharacterMaxBattlePower = 7011000
    # [Description("キャラクター達成レベル")]
    CharacterCharacterMaxLevel = 7011100
    # [Description("武具強化最大達成レベル")]
    CharacterAllEquipmentReinforceMaxLevel = 7011200
    # [Description("キャラクター最高到達レアリティ")]
    CharacterRankUpMaxRarity = 7020100
    # [Description("キャラクター進化回数")]
    CharacterRankUpEvolutionCount = 7020200
    # [Description("レベルリンク枠解放数")]
    CharacterLevelLinkOpenSlotCount = 7030100
    # [Description("最高所持スフィアレベル")]
    EquipmentSphereMaxLevel = 8010100
    # [Description("スフィア合成回数")]
    EquipmentSphereComposeCount = 8010200
    # [Description("精錬武具（武具鋳造）個数")]
    EquipmentForgeCount = 8020100
    # [Description("Rナヘマー武具シリーズ合成回数")]
    EquipmentComposeCountR = 8030101
    # [Description("SRサンダルフォン武具シリーズ合成回数")]
    EquipmentComposeCountSR = 8030102
    # [Description("SSRアスタロト武具シリーズ合成回数")]
    EquipmentComposeCountSSR = 8030103
    # [Description("プレイヤー達成レベル")]
    AutoBattleMaxPlayerLevel = 9010100
    # [Description("獲得した合計領民数")]
    AutoBattleAddPopulation = 9010200
    # [Description("ボス勝利回数")]
    BossBattleVictoryCount = 9010300
    # [Description("最高到達クエスト")]
    AutoBattleMaxClearQuest = 9010400
    # [Description("最高到達章")]
    AutoBattledMaxClearChapter = 9010500
    # [Description("放置バトル報酬受け取り回数")]
    AutoBattleGetRewardCount = 9010600
    # [Description("高速バトル回数")]
    AutoBattleQuickCount = 9020100
    # [Description("時空の洞窟階層3クリア回数")]
    DungeonBattleClearThirdFloorCount = 10010100
    # [Description("時空の洞窟階層1クリア回数")]
    DungeonBattleClearFirstFloorCount = 10010200
    # [Description("時空の洞窟で〇人以上の○○タイプのキャラを使って戦闘に勝利")]
    DungeonBattleClearUnitJobTypeBase = 10010300
    # [Description("時空の洞窟で1人以上のウォリアータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear1UnitWarriorType = 10010311
    # [Description("時空の洞窟で1人以上のスナイパータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear1UnitSniperType = 10010312
    # [Description("時空の洞窟で1人以上のソーサラータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear1UnitSorcererType = 10010314
    # [Description("時空の洞窟で2人以上のウォリアータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear2UnitWarriorType = 10010321
    # [Description("時空の洞窟で2人以上のスナイパータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear2UnitSniperType = 10010322
    # [Description("時空の洞窟で2人以上のソーサラータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear2UnitSorcererType = 10010324
    # [Description("時空の洞窟で3人以上のウォリアータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear3UnitWarriorType = 10010331
    # [Description("時空の洞窟で3人以上のスナイパータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear3UnitSniperType = 10010332
    # [Description("時空の洞窟で3人以上のソーサラータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear3UnitSorcererType = 10010334
    # [Description("時空の洞窟で4人以上のウォリアータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear4UnitWarriorType = 10010341
    # [Description("時空の洞窟で4人以上のスナイパータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear4UnitSniperType = 10010342
    # [Description("時空の洞窟で4人以上のソーサラータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear4UnitSorcererType = 10010344
    # [Description("時空の洞窟で5人以上のウォリアータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear5UnitWarriorType = 10010351
    # [Description("時空の洞窟で5人以上のスナイパータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear5UnitSniperType = 10010352
    # [Description("時空の洞窟で5人以上のソーサラータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear5UnitSorcererType = 10010354
    # [Description("時空の洞窟新キャラミッション")]
    DungeonBattleNewCharacter = 10011000
    # [Description("無窮の塔階層クリア数")]
    TowerBattleMaxClearFloor = 11010100
    # [Description("属性の塔到達下限階層")]
    TowerBattleMinClearElementTower = 11010200
    # [Description("無窮の塔勝利回数")]
    TowerBattleTotalWinCount = 11010300
    # [Description("バトルリーグ挑戦回数")]
    BattleLeagueChallengeCount = 12010100
    # [Description("バトルリーグ最高順位")]
    BattleLeagueMaxRanking = 12010200
    # [Description("幻影の神殿勝利回数")]
    LocalRaidVictoryCount = 13010100
    # [Description("祈りの泉クエスト受領回数")]
    BountyQuestAllStartQuestCount = 14010100
    # [Description("祈りの泉新キャラミッション")]
    BountyQuestNewCharacter = 14011000
    # [Description("祈りの泉マルチクエスト受領回数")]
    BountyQuestTeamStartQuestCount = 14020100
    # [Description("キャラ入手数")]
    GachaNewJoinCharacter = 15010100
    # [Description("キャラガチャ回数")]
    GachaDrawCount = 15010200
    # [Description("ダイヤ消費量")]
    ConsumeCurrencyCount = 15010300
    # [Description("ギルド加入回数")]
    GuildJoinCount = 16010100
    # [Description("ギルドログイン回数")]
    GuildLoginCount = 16010200
    # [Description("ギルドレイド回数（解放ボス含む）")]
    GuildGuildRaidChallengeCount = 16020100
    # [Description("ワールドチャット発言回数")]
    ChatSayWorldChatCount = 17010100
    # [Description("アップデート回数")]
    OsStoreUpdateCount = 18010100

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

class TimelineType(Enum):
    MyPage = 0
    Battle = 1
    Skill = 2
    SkillQlipha = 3
    Memory = 4
    MyPageQlipha = 5

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("パラメーター増減タイプ")]
class ChangeParameterType(Enum):
    # [Description("加算(+X)")]
    Addition = 1
    # [Description("乗算(+X%)")]
    AdditionPercent = 2
    # [Description("キャラLv×係数")]
    CharacterLevelConstantMultiplicationAddition = 3

# [Description("バトルパラメータの種類")]
class BattleParameterType(Enum):
    # [Description("HP")]
    Hp = 1
    # [Description("攻撃力")]
    AttackPower = 2
    # [Description("物理ダメージ緩和")]
    PhysicalDamageRelax = 3
    # [Description("魔法ダメージ緩和")]
    MagicDamageRelax = 4
    # [Description("命中")]
    Hit = 5
    # [Description("回避")]
    Avoidance = 6
    # [Description("クリティカル")]
    Critical = 7
    # [Description("クリティカル耐性")]
    CriticalResist = 8
    # [Description("クリダメ強化")]
    CriticalDamageEnhance = 9
    # [Description("物理クリダメ緩和")]
    PhysicalCriticalDamageRelax = 10
    # [Description("魔法クリダメ緩和")]
    MagicCriticalDamageRelax = 11
    # [Description("防御貫通力")]
    DefensePenetration = 12
    # [Description("防御力")]
    Defense = 13
    # [Description("物魔防御貫通")]
    DamageEnhance = 14
    # [Description("弱体効果命中")]
    DebuffHit = 15
    # [Description("弱体効果耐性")]
    DebuffResist = 16
    # [Description("リフレクト")]
    DamageReflect = 17
    # [Description("HP吸収")]
    HpDrain = 18
    # [Description("スピード")]
    Speed = 19

# [Description("パラメーター増減タイプ")]
class ChangeParameterType(Enum):
    # [Description("加算(+X)")]
    Addition = 1
    # [Description("乗算(+X%)")]
    AdditionPercent = 2
    # [Description("キャラLv×係数")]
    CharacterLevelConstantMultiplicationAddition = 3

# [Description("基礎パラメータの種類")]
class BaseParameterType(Enum):
    # [Description("筋力")]
    Muscle = 1
    # [Description("技力")]
    Energy = 2
    # [Description("魔力")]
    Intelligence = 3
    # [Description("耐久力")]
    Health = 4

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("懸賞カウンタータイプ")]
class BountyQuestType(Enum):
    # [Description("ソロ")]
    Solo = 0
    # [Description("チーム")]
    Team = 1
    # [Description("ゲリラ")]
    Guerrilla = 2

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("祈りの泉クエストレアリティ")]
# [Flags]
class BountyQuestRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("N*")]
    NInit = 1
    # [Description("N")]
    N = 2
    # [Description("R")]
    R = 4
    # [Description("SR")]
    SR = 8
    # [Description("SSR")]
    SSR = 16
    # [Description("UR")]
    UR = 32
    # [Description("LR")]
    LR = 64

# [Description("懸賞カウンタータイプ")]
class BountyQuestType(Enum):
    # [Description("ソロ")]
    Solo = 0
    # [Description("チーム")]
    Team = 1
    # [Description("ゲリラ")]
    Guerrilla = 2

# [Description("武具のレアリティ")]
# [Flags]
class EquipmentRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("D")]
    D = 1
    # [Description("C")]
    C = 2
    # [Description("B")]
    B = 4
    # [Description("A")]
    A = 8
    # [Description("S")]
    S = 16
    # [Description("R")]
    R = 32
    # [Description("SR")]
    SR = 64
    # [Description("SSR")]
    SSR = 128
    # [Description("UR")]
    UR = 256
    # [Description("LR")]
    LR = 512

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [MessagePackObject(True)]
@dataclass
class VipGiftInfo():
    # [Description("獲得アイテムリスト")]
    # [Nest(True, 1)]
    GetItemList: list[UserItem]
    # [Description("必要アイテムリスト")]
    # [Nest(True, 1)]
    RequiredItemList: list[UserItem]
    # [Description("ギフトID")]
    VipGiftId: int

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("ページ情報")]
# [MessagePackObject(True)]
@dataclass
class TutorialDescriptionPageInfo():
    # [Description("画像ID")]
    # [PropertyOrder(2)]
    ImageId: int
    # [Description("本文")]
    # [PropertyOrder(1)]
    MainTextKey: str

# [Description("画像位置フォーマット")]
class ImagePositionFormatType(Enum):
    # [Description("不明")]
    None_ = 0
    # [Description("時空の洞窟イベント")]
    DungeonBattleEvent = 1
    # [Description("神殿イベント")]
    LocalRaidEvent = 2

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("宝箱抽選タイプ")]
class TreasureChestLotteryType(Enum):
    # [Description("抽選で1つ")]
    Random = 0
    # [Description("固定で1つ")]
    Static = 1
    # [Description("キャラクター1つを選択")]
    SelectCharacter = 2
    # [Description("アイテム1つを選択")]
    SelectItem = 3
    # [Description("選択した中から抽選")]
    SelectRandom = 4
    # [Description("複数の固定アイテム")]
    Fix = 5
    # [Description("抽選アイテムと固定アイテム")]
    RandomFix = 6

# [Description("第2フレーム種類")]
class SecondaryFrameType(Enum):
    # [Description("不明")]
    None_ = 0
    # [Description("属性アイコン")]
    ElementIcon = 1
    # [Description("効果時間表示")]
    EffectTime = 2
    # [Description("レベル")]
    Level = 3
    # [Description("キャラアイコン_中央")]
    CenteredCharacterIcon = 4

# [Description("アイテムのレアリティ")]
# [Flags]
class ItemRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("D")]
    D = 1
    # [Description("C")]
    C = 2
    # [Description("B")]
    B = 4
    # [Description("A")]
    A = 8
    # [Description("S")]
    S = 16
    # [Description("R")]
    R = 32
    # [Description("SR")]
    SR = 64
    # [Description("SSR")]
    SSR = 128
    # [Description("UR")]
    UR = 256
    # [Description("LR")]
    LR = 512

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

class TreasureChestItemListType(Enum):
    None_ = 0
    TreasureChestItemList = 1
    GachaLotteryItemList = 2
    SelectItemList = 3

# [Description("宝箱選択アイテム")]
# [MessagePackObject(True)]
@dataclass
class TreasureChestSelectItem():
    # [Description("アイテム")]
    # [Nest(True, 1)]
    SelectItem: UserItem
    # [Description("神器タイプ")]
    SacredTreasureType: SacredTreasureType

# [Description("宝箱固定アイテム")]
# [MessagePackObject(True)]
@dataclass
class TreasureChestFixItem():
    # [Description("アイテム")]
    # [Nest(True, 2)]
    FixItem: UserItem
    # [Description("神器タイプ")]
    SacredTreasureType: SacredTreasureType

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("交換所種類")]
class TradeShopType(Enum):
    # [Description("一般")]
    Normal = 0
    # [Description("通常武具合成")]
    NormalEquipmentComposite = 1
    # [Description("パターン2")]
    Fix = 2
    # [Description("店舗")]
    Store = 3
    # [Description("スフィア")]
    Sphere = 4

# [Description("解放されるコマンドの種類")]
class OpenCommandType(Enum):
    # [Description("コマンド無し")]
    None_ = 0
    # [Description("アルカナ")]
    Arcana = 1
    # [Description("ショップ")]
    Shop = 2
    # [Description("ミッション")]
    Mission = 3
    # [Description("時空の洞窟")]
    DungeonBattle = 4
    # [Description("バトルスキップ")]
    BattleSkip = 5
    # [Description("バトル倍速")]
    BattleSpeed = 6
    # [Description("バトル4倍速")]
    BattleSpeed4 = 7
    # [Description("時空の洞窟 見逃し補填")]
    DungeonBattleCompensation = 8
    # [Description("無窮の塔")]
    TowerBattle = 9
    # [Description("祈りの泉")]
    BountyQuest = 10
    # [Description("バトルリーグ")]
    BattleLeague = 11
    # [Description("幻影の神殿")]
    LocalRaid = 12
    # [Description("レジェンドリーグ")]
    LegendLeague = 13
    # [Description("運命ガチャ")]
    GachaDestiny = 14
    # [Description("エスペリアタワー")]
    EsperiaTower = 15
    # [Description("洞窟バトルハードモード")]
    DungeonBattleHardMode = 16
    # [Description("メモリー")]
    CharacterStory = 17
    # [Description("ロイヤルショップ")]
    RoyalShop = 18
    # [Description("ランキング")]
    Ranking = 19
    # [Description("スフィア装着")]
    SphereSet = 20
    # [Description("武具合成通常")]
    ShopNormalEquipment = 21
    # [Description("武具合成聖装")]
    ShopLegendEquipment = 22
    # [Description("ギルド（GVG）")]
    ShopGuild = 23
    # [Description("キャラコインショップ")]
    ShopCharacter = 24
    # [Description("時空の洞窟")]
    ShopDungeonBattle = 25
    # [Description("バトルリーグ")]
    ShopBattleLeague = 26
    # [Description("レジェンドリーグ")]
    ShopLegendLeague = 27
    # [Description("限定特典")]
    ShopLimited = 28
    # [Description("進化")]
    RankUp = 29
    # [Description("プレゼント")]
    Present = 30
    # [Description("武具強化")]
    EquipmentStrength = 31
    # [Description("神装強化")]
    EquipmentAscend = 32
    # [Description("武具進化")]
    EquipmentEvolution = 33
    # [Description("祈りの泉一括派遣、受け取り")]
    BountyQuestQuick = 34
    # [Description("ギルドレイドの掃討")]
    GuildRaidQuick = 35
    # [Description("ボス/無窮の塔掃討")]
    BossBattleQuick = 36
    # [Description("武具ガチャ")]
    GachaEquipment = 37
    # [Description("武具研磨")]
    EquipmentRefine = 38
    # [Description("フレンド")]
    Friend = 39
    # [Description("マイページ")]
    FooterMyPage = 40
    # [Description("キャラ")]
    FooterCharacter = 41
    # [Description("アイテムボックス")]
    FooterItemBox = 42
    # [Description("試練")]
    FooterCompetition = 43
    # [Description("ガチャ")]
    FooterGacha = 44
    # [Description("チャット")]
    FooterChat = 45
    # [Description("ギルド")]
    FooterGuild = 46
    # [Description("魔水晶（ショップ）&キャラ詳細_専用武器交換")]
    ShopMagicCrystal = 47
    # [Description("聖遺物（ショップ）")]
    ShopRelics = 48
    # [Description("スフィア（ショップ）")]
    ShopSphere = 49
    # [Description("イベント（ショップ）")]
    ShopEventExchange = 50
    # [Description("グランドバトル（ショップ）")]
    ShopGrandBattle = 51
    # [Description("レベルリンク")]
    LevelLink = 80
    # [Description("チュートリアルスキップ")]
    SkipTutorial = 100
    # [Description("月間ログインボーナス")]
    MonthlyLoginBonus = 120
    # [Description("期間限定ログインボーナス")]
    LimitedLoginBonus = 121
    # [Description("第二大陸")]
    SecondContinent = 140
    # [Description("フレンドコード")]
    FriendCode = 200

# [MessagePackObject(True)]
@dataclass
class CustomTextLayout():
    # [Description("英語")]
    # [Nest(True, 2)]
    # [PropertyOrder(2)]
    enUS: CustomTextLayoutInfo
    # [Description("日本語")]
    # [Nest(True, 2)]
    # [PropertyOrder(1)]
    jaJP: CustomTextLayoutInfo
    # [Description("韓国語")]
    # [Nest(True, 2)]
    # [PropertyOrder(3)]
    koKR: CustomTextLayoutInfo
    # [Description("中国語(繁体字)")]
    # [Nest(True, 2)]
    # [PropertyOrder(5)]
    zhTW: CustomTextLayoutInfo

# [MessagePackObject(True)]
@dataclass
class ConsumeItemInfo():
    # [Description("アイテムの種類")]
    ItemType: ItemType
    # [Description("アイテムのID")]
    ItemId: int

# [Description("定期自動更新タイプ")]
class TradeShopAutoUpdateType(Enum):
    # [Description("定期自動更新なし")]
    None_ = 0
    # [Description("1日1回、4時に更新")]
    OneDay = 1
    # [Description("1週間に1回、4時に更新")]
    OneWeek = 2
    # [Description("1カ月に1回、4時に更新")]
    OneMonth = 3
    # [Description("1日に複数回、指定時刻に更新")]
    SetTime = 4

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("無窮の塔タイプ")]
class TowerType(Enum):
    None_ = 0
    # [Description("無窮の塔")]
    Infinite = 1
    # [Description("愁（しゅう）")]
    Blue = 2
    # [Description("業（ごう）")]
    Red = 3
    # [Description("心（しん）")]
    Green = 4
    # [Description("渇（かつ）")]
    Yellow = 5

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

class UnitIconType(Enum):
    # [Description("キャラクター")]
    Character = 0
    # [Description("敵キャラクター")]
    EnemyCharacter = 1
    # [Description("魔女クリファ")]
    WitchQlipha = 2

# [Description("職業")]
# [Flags]
class JobFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("ウォリアー")]
    Warrior = 1
    # [Description("スナイパー")]
    Sniper = 2
    # [Description("ソーサラー")]
    Sorcerer = 4

class ElementType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("愁（しゅう）")]
    Blue = 1
    # [Description("業（ごう）")]
    Red = 2
    # [Description("心（しん）")]
    Green = 3
    # [Description("渇（かつ）")]
    Yellow = 4
    # [Description("天（てん） ")]
    Light = 5
    # [Description("冥（めい） ")]
    Dark = 6

# [Description("キャラクターのレアリティ")]
# [Flags]
class CharacterRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("N")]
    N = 1
    # [Description("R")]
    R = 2
    # [Description("R+")]
    RPlus = 4
    # [Description("SR")]
    SR = 8
    # [Description("SR+")]
    SRPlus = 16
    # [Description("SSR")]
    SSR = 32
    # [Description("SSR+")]
    SSRPlus = 64
    # [Description("UR")]
    UR = 128
    # [Description("UR+")]
    URPlus = 256
    # [Description("LR")]
    LR = 512
    # [Description("LR+")]
    LRPlus = 1024
    # [Description("LR+2")]
    LRPlus2 = 2048
    # [Description("LR+3")]
    LRPlus3 = 4096
    # [Description("LR+4")]
    LRPlus4 = 8192
    # [Description("LR+5")]
    LRPlus5 = 16384
    # [Description("LR+6")]
    LRPlus6 = 32768
    # [Description("LR+7")]
    LRPlus7 = 65536

# [Description("バトルパラメータ")]
# [MessagePackObject(True)]
@dataclass
class BattleParameter():
    # [Description("攻撃力")]
    AttackPower: int
    # [Description("回避")]
    Avoidance: int
    # [Description("クリティカル")]
    Critical: int
    # [Description("クリダメ強化")]
    CriticalDamageEnhance: int
    # [Description("クリティカル耐性")]
    CriticalResist: int
    # [Description("ダメージ強化")]
    DamageEnhance: int
    # [Description("カウンタ​")]
    DamageReflect: int
    # [Description("弱体効果命中​")]
    DebuffHit: int
    # [Description("弱体効果耐性")]
    DebuffResist: int
    # [Description("防御力")]
    Defense: int
    # [Description("防御貫通力")]
    DefensePenetration: int
    # [Description("命中")]
    Hit: int
    # [Description("HP")]
    HP: int
    # [Description("HP吸収")]
    HpDrain: int
    # [Description("魔法クリダメ緩和")]
    MagicCriticalDamageRelax: int
    # [Description("魔法ダメージ緩和")]
    MagicDamageRelax: int
    # [Description("物理クリダメ緩和")]
    PhysicalCriticalDamageRelax: int
    # [Description("物理ダメージ緩和")]
    PhysicalDamageRelax: int
    # [Description("スピード​")]
    Speed: int

# [Description("基礎パラメータ")]
# [MessagePackObject(True)]
@dataclass
class BaseParameter():
    # [Description("技力​")]
    Energy: int
    # [Description("耐久力​")]
    Health: int
    # [Description("魔力")]
    Intelligence: int
    # [Description("筋力")]
    Muscle: int

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [MessagePackObject(True)]
@dataclass
class EventMissionReward():
    # [Nest(True, 1)]
    # [PropertyOrder(1)]
    EventItem: UserItem
    # [PropertyOrder(2)]
    RarityFlags: CharacterRarityFlags

# [MessagePackObject(True)]
@dataclass
class MissionReward():
    # [Nest(True, 1)]
    # [PropertyOrder(1)]
    Item: UserItem
    # [PropertyOrder(2)]
    RarityFlags: CharacterRarityFlags

# [Description("ミッショングループ")]
class MissionGroupType(Enum):
    # [Description("メイン")]
    Main = 0
    # [Description("デイリー")]
    Daily = 1
    # [Description("ウィークリー")]
    Weekly = 2
    # [Description("初心者")]
    Beginner = 3
    # [Description("カムバック")]
    Comeback = 4
    # [Description("新キャラ")]
    NewCharacter = 5
    # [Description("イベント")]
    Limited = 6

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("解放されるコマンドの種類")]
class OpenCommandType(Enum):
    # [Description("コマンド無し")]
    None_ = 0
    # [Description("アルカナ")]
    Arcana = 1
    # [Description("ショップ")]
    Shop = 2
    # [Description("ミッション")]
    Mission = 3
    # [Description("時空の洞窟")]
    DungeonBattle = 4
    # [Description("バトルスキップ")]
    BattleSkip = 5
    # [Description("バトル倍速")]
    BattleSpeed = 6
    # [Description("バトル4倍速")]
    BattleSpeed4 = 7
    # [Description("時空の洞窟 見逃し補填")]
    DungeonBattleCompensation = 8
    # [Description("無窮の塔")]
    TowerBattle = 9
    # [Description("祈りの泉")]
    BountyQuest = 10
    # [Description("バトルリーグ")]
    BattleLeague = 11
    # [Description("幻影の神殿")]
    LocalRaid = 12
    # [Description("レジェンドリーグ")]
    LegendLeague = 13
    # [Description("運命ガチャ")]
    GachaDestiny = 14
    # [Description("エスペリアタワー")]
    EsperiaTower = 15
    # [Description("洞窟バトルハードモード")]
    DungeonBattleHardMode = 16
    # [Description("メモリー")]
    CharacterStory = 17
    # [Description("ロイヤルショップ")]
    RoyalShop = 18
    # [Description("ランキング")]
    Ranking = 19
    # [Description("スフィア装着")]
    SphereSet = 20
    # [Description("武具合成通常")]
    ShopNormalEquipment = 21
    # [Description("武具合成聖装")]
    ShopLegendEquipment = 22
    # [Description("ギルド（GVG）")]
    ShopGuild = 23
    # [Description("キャラコインショップ")]
    ShopCharacter = 24
    # [Description("時空の洞窟")]
    ShopDungeonBattle = 25
    # [Description("バトルリーグ")]
    ShopBattleLeague = 26
    # [Description("レジェンドリーグ")]
    ShopLegendLeague = 27
    # [Description("限定特典")]
    ShopLimited = 28
    # [Description("進化")]
    RankUp = 29
    # [Description("プレゼント")]
    Present = 30
    # [Description("武具強化")]
    EquipmentStrength = 31
    # [Description("神装強化")]
    EquipmentAscend = 32
    # [Description("武具進化")]
    EquipmentEvolution = 33
    # [Description("祈りの泉一括派遣、受け取り")]
    BountyQuestQuick = 34
    # [Description("ギルドレイドの掃討")]
    GuildRaidQuick = 35
    # [Description("ボス/無窮の塔掃討")]
    BossBattleQuick = 36
    # [Description("武具ガチャ")]
    GachaEquipment = 37
    # [Description("武具研磨")]
    EquipmentRefine = 38
    # [Description("フレンド")]
    Friend = 39
    # [Description("マイページ")]
    FooterMyPage = 40
    # [Description("キャラ")]
    FooterCharacter = 41
    # [Description("アイテムボックス")]
    FooterItemBox = 42
    # [Description("試練")]
    FooterCompetition = 43
    # [Description("ガチャ")]
    FooterGacha = 44
    # [Description("チャット")]
    FooterChat = 45
    # [Description("ギルド")]
    FooterGuild = 46
    # [Description("魔水晶（ショップ）&キャラ詳細_専用武器交換")]
    ShopMagicCrystal = 47
    # [Description("聖遺物（ショップ）")]
    ShopRelics = 48
    # [Description("スフィア（ショップ）")]
    ShopSphere = 49
    # [Description("イベント（ショップ）")]
    ShopEventExchange = 50
    # [Description("グランドバトル（ショップ）")]
    ShopGrandBattle = 51
    # [Description("レベルリンク")]
    LevelLink = 80
    # [Description("チュートリアルスキップ")]
    SkipTutorial = 100
    # [Description("月間ログインボーナス")]
    MonthlyLoginBonus = 120
    # [Description("期間限定ログインボーナス")]
    LimitedLoginBonus = 121
    # [Description("第二大陸")]
    SecondContinent = 140
    # [Description("フレンドコード")]
    FriendCode = 200

# [Description("遷移先")]
class ViewTransitionType(Enum):
    # [Description("キャラ育成")]
    CharacterTraining = 0
    # [Description("キャラランクアップ")]
    CharacterRankUp = 1
    # [Description("遷移なしの編成ダイアログ")]
    FormationWithoutTransition = 2
    # [Description("放置バトルMAP")]
    Map = 3
    # [Description("ミッション")]
    Mission = 4

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("言語")]
class LanguageType(Enum):
    None_ = 0
    # [Description("日本語")]
    jaJP = 1
    # [Description("英語")]
    enUS = 2
    # [Description("韓国語")]
    koKR = 3
    # [Description("中国語(繁体字)")]
    zhTW = 4

# [Description("言語")]
class LanguageType(Enum):
    None_ = 0
    # [Description("日本語")]
    jaJP = 1
    # [Description("英語")]
    enUS = 2
    # [Description("韓国語")]
    koKR = 3
    # [Description("中国語(繁体字)")]
    zhTW = 4

# [Description("時差グループ")]
class TimeServerType(Enum):
    None_ = 0
    # [Description("日本")]
    JP = 1
    # [Description("韓国")]
    KR = 2
    # [Description("アジア")]
    Asia = 3
    # [Description("アメリカ")]
    US = 4
    # [Description("ヨーロッパ")]
    EU = 5
    # [Description("グローバル")]
    Global = 6

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("規約ボタン情報")]
# [MessagePackObject(True)]
@dataclass
class TermsButtonInfo():
    # [Description("ボタンテキストKey")]
    # [PropertyOrder(1)]
    Name: str
    # [Description("Url")]
    # [PropertyOrder(2)]
    Url: str

# [Description("規約ボタン情報")]
# [MessagePackObject(True)]
@dataclass
class TermsButtonInfo():
    # [Description("ボタンテキストKey")]
    # [PropertyOrder(1)]
    Name: str
    # [Description("Url")]
    # [PropertyOrder(2)]
    Url: str

# [Description("規約ボタン情報")]
# [MessagePackObject(True)]
@dataclass
class TermsButtonInfo():
    # [Description("ボタンテキストKey")]
    # [PropertyOrder(1)]
    Name: str
    # [Description("Url")]
    # [PropertyOrder(2)]
    Url: str

# [Description("規約ボタン情報")]
# [MessagePackObject(True)]
@dataclass
class TermsButtonInfo():
    # [Description("ボタンテキストKey")]
    # [PropertyOrder(1)]
    Name: str
    # [Description("Url")]
    # [PropertyOrder(2)]
    Url: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("Steam価格表情報")]
# [MessagePackObject(True)]
@dataclass
class SteamProductPriceInfo():
    # [Description("通貨コード")]
    CurrencyCode: str
    # [Description("表示倍率")]
    Multiple: float
    # [Description("価格")]
    ProductPrice: int

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("累計貢献メダル報酬ボーナス情報")]
# [MessagePackObject(True)]
@dataclass
class TotalActivityMedalRewardBonus():
    # [Description("ボーナス報酬リスト")]
    # [Nest(True, 1)]
    # [PropertyOrder(2)]
    BonusRewardList: list[MissionReward]
    # [Description("累計貢献メダル報酬ID")]
    # [PropertyOrder(1)]
    TotalActivityMedalRewardId: int

# [Description("アイテムアイコン情報")]
# [MessagePackObject(True)]
@dataclass
class ItemIconInfo():
    # [Description("アイテムID")]
    # [PropertyOrder(1)]
    ItemId: int
    # [Description("アイテムタイプ")]
    # [PropertyOrder(2)]
    ItemType: ItemType

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

class SphereType(Enum):
    EquipmentIcon = 0
    Small = 1
    Medium = 2
    Large = 3

# [Description("アイテムのレアリティ")]
# [Flags]
class ItemRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("D")]
    D = 1
    # [Description("C")]
    C = 2
    # [Description("B")]
    B = 4
    # [Description("A")]
    A = 8
    # [Description("S")]
    S = 16
    # [Description("R")]
    R = 32
    # [Description("SR")]
    SR = 64
    # [Description("SSR")]
    SSR = 128
    # [Description("UR")]
    UR = 256
    # [Description("LR")]
    LR = 512

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [Description("バトルパラメータ変動情報")]
# [MessagePackObject(True)]
@dataclass
class BattleParameterChangeInfo():
    # [Description("変動するバトルパラメータ")]
    # [PropertyOrder(1)]
    BattleParameterType: BattleParameterType
    # [Description("パラメータ増減タイプ")]
    # [PropertyOrder(2)]
    ChangeParameterType: ChangeParameterType
    # [Description("値")]
    # [PropertyOrder(3)]
    Value: float

# [Description("基礎パラメータ変動情報")]
# [MessagePackObject(True)]
@dataclass
class BaseParameterChangeInfo():
    # [Description("変動する基礎パラメータ")]
    # [PropertyOrder(1)]
    BaseParameterType: BaseParameterType
    # [Description("パラメータ増減タイプ")]
    # [PropertyOrder(2)]
    ChangeParameterType: ChangeParameterType
    # [Description("値")]
    # [PropertyOrder(3)]
    Value: float

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("クエスト難易度")]
class QuestDifficultyType(Enum):
    # [Description("Easy")]
    Easy = 0
    # [Description("Hard")]
    Hard = 1

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [Description("PvPランキング報酬タイプ")]
class PvpRankingRewardType(Enum):
    # [Description("バトルリーグデイリーランキング報酬")]
    BattleLeagueDailyRankingReward = 0
    # [Description("レジェンドリーグデイリーランキング報酬")]
    LegendLeagueDailyRankingReward = 1
    # [Description("レジェンドリーグシーズンランキング報酬")]
    LegendLeagueSeasonRankingReward = 2

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [MessagePackObject(True)]
@dataclass
class PassiveSkillInfo():
    # [Description("優先順位")]
    OrderNumber: int
    # [Description("スキル説明文キー")]
    DescriptionKey: str
    # [Description("キャラクターレベル制限")]
    CharacterLevel: int
    # [Description("専属武具レアリティ")]
    EquipmentRarityFlags: EquipmentRarityFlags
    # [Description("加護ID")]
    BlessingItemId: int
    # [Description("パッシブサブセット情報")]
    # [Nest(True, 2)]
    PassiveSubSetSkillInfos: list[PassiveSubSetSkillInfo]

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("コンテンツ開放タイプ")]
class OpenContentType(Enum):
    # [Description("ランクアップ")]
    RankUp = 0
    # [Description("クエストクリア")]
    QuestClear = 1
    # [Description("グランドバトル参加チェック")]
    AfterStartGrandBattle = 2

# [Description("解放されるコマンドの種類")]
class OpenCommandType(Enum):
    # [Description("コマンド無し")]
    None_ = 0
    # [Description("アルカナ")]
    Arcana = 1
    # [Description("ショップ")]
    Shop = 2
    # [Description("ミッション")]
    Mission = 3
    # [Description("時空の洞窟")]
    DungeonBattle = 4
    # [Description("バトルスキップ")]
    BattleSkip = 5
    # [Description("バトル倍速")]
    BattleSpeed = 6
    # [Description("バトル4倍速")]
    BattleSpeed4 = 7
    # [Description("時空の洞窟 見逃し補填")]
    DungeonBattleCompensation = 8
    # [Description("無窮の塔")]
    TowerBattle = 9
    # [Description("祈りの泉")]
    BountyQuest = 10
    # [Description("バトルリーグ")]
    BattleLeague = 11
    # [Description("幻影の神殿")]
    LocalRaid = 12
    # [Description("レジェンドリーグ")]
    LegendLeague = 13
    # [Description("運命ガチャ")]
    GachaDestiny = 14
    # [Description("エスペリアタワー")]
    EsperiaTower = 15
    # [Description("洞窟バトルハードモード")]
    DungeonBattleHardMode = 16
    # [Description("メモリー")]
    CharacterStory = 17
    # [Description("ロイヤルショップ")]
    RoyalShop = 18
    # [Description("ランキング")]
    Ranking = 19
    # [Description("スフィア装着")]
    SphereSet = 20
    # [Description("武具合成通常")]
    ShopNormalEquipment = 21
    # [Description("武具合成聖装")]
    ShopLegendEquipment = 22
    # [Description("ギルド（GVG）")]
    ShopGuild = 23
    # [Description("キャラコインショップ")]
    ShopCharacter = 24
    # [Description("時空の洞窟")]
    ShopDungeonBattle = 25
    # [Description("バトルリーグ")]
    ShopBattleLeague = 26
    # [Description("レジェンドリーグ")]
    ShopLegendLeague = 27
    # [Description("限定特典")]
    ShopLimited = 28
    # [Description("進化")]
    RankUp = 29
    # [Description("プレゼント")]
    Present = 30
    # [Description("武具強化")]
    EquipmentStrength = 31
    # [Description("神装強化")]
    EquipmentAscend = 32
    # [Description("武具進化")]
    EquipmentEvolution = 33
    # [Description("祈りの泉一括派遣、受け取り")]
    BountyQuestQuick = 34
    # [Description("ギルドレイドの掃討")]
    GuildRaidQuick = 35
    # [Description("ボス/無窮の塔掃討")]
    BossBattleQuick = 36
    # [Description("武具ガチャ")]
    GachaEquipment = 37
    # [Description("武具研磨")]
    EquipmentRefine = 38
    # [Description("フレンド")]
    Friend = 39
    # [Description("マイページ")]
    FooterMyPage = 40
    # [Description("キャラ")]
    FooterCharacter = 41
    # [Description("アイテムボックス")]
    FooterItemBox = 42
    # [Description("試練")]
    FooterCompetition = 43
    # [Description("ガチャ")]
    FooterGacha = 44
    # [Description("チャット")]
    FooterChat = 45
    # [Description("ギルド")]
    FooterGuild = 46
    # [Description("魔水晶（ショップ）&キャラ詳細_専用武器交換")]
    ShopMagicCrystal = 47
    # [Description("聖遺物（ショップ）")]
    ShopRelics = 48
    # [Description("スフィア（ショップ）")]
    ShopSphere = 49
    # [Description("イベント（ショップ）")]
    ShopEventExchange = 50
    # [Description("グランドバトル（ショップ）")]
    ShopGrandBattle = 51
    # [Description("レベルリンク")]
    LevelLink = 80
    # [Description("チュートリアルスキップ")]
    SkipTutorial = 100
    # [Description("月間ログインボーナス")]
    MonthlyLoginBonus = 120
    # [Description("期間限定ログインボーナス")]
    LimitedLoginBonus = 121
    # [Description("第二大陸")]
    SecondContinent = 140
    # [Description("フレンドコード")]
    FriendCode = 200

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("合計ログイン報酬情報")]
# [MessagePackObject(True)]
@dataclass
class LoginCountRewardInfo():
    # [Description("合計ログイン日数")]
    # [PropertyOrder(1)]
    DayCount: int
    # [Description("画像パス")]
    # [PropertyOrder(3)]
    ImagePath: str
    # [Description("画像X座標")]
    # [PropertyOrder(4)]
    PositionX: int
    # [Description("合計ログイン報酬リスト")]
    # [Nest(True, 1)]
    # [PropertyOrder(2)]
    RewardItemList: list[UserItem]

# [Description("日別ログイン報酬情報")]
# [MessagePackObject(True)]
@dataclass
class LoginDailyRewardInfo():
    # [Description("日数")]
    # [PropertyOrder(1)]
    Day: int
    # [Description("日別ログイン報酬")]
    # [Nest(True, 1)]
    # [PropertyOrder(2)]
    RewardItem: UserItem

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("ミッションタイプ")]
class MissionType(Enum):
    Main = 0
    Daily = 1
    Weekly = 2
    BeginnerFirstDay = 311
    BeginnerFirstDayLevel = 312
    BeginnerFirstDayStage = 313
    BeginnerFirstDayBuy = 314
    BeginnerSecondDay = 321
    BeginnerSecondDayQuick = 322
    BeginnerSecondDayBattleLeague = 323
    BeginnerSecondDayBuy = 324
    BeginnerThirdDay = 331
    BeginnerThirdDayForge = 332
    BeginnerThirdDayDungeonBattle = 333
    BeginnerThirdDayBuy = 334
    BeginnerFourthDay = 341
    BeginnerFourthDayReinforceEquipment = 342
    BeginnerFourthDayTowerBattle = 343
    BeginnerFourthDayBuy = 344
    BeginnerFifthDay = 351
    BeginnerFifthDayBountyQuest = 352
    BeginnerFifthDayTotalCharacter = 353
    BeginnerFifthDayBuy = 354
    BeginnerSixthDay = 361
    BeginnerSixthDaySphere = 362
    BeginnerSixthDayCharacterEvolution = 363
    BeginnerSixthDayBuy = 364
    BeginnerSeventhDay = 371
    BeginnerSeventhDayTraining = 372
    BeginnerSeventhDayLocalRaid = 373
    BeginnerSeventhDayBuy = 374
    ComebackLogin = 401
    ComebackActivity = 402
    ComebackConsumeCurrency = 403
    NewCharacter = 5
    LimitedFirstDayTab1 = 611
    LimitedFirstDayTab2 = 612
    LimitedFirstDayTab3 = 613
    LimitedFirstDayTab4 = 614
    LimitedSecondDayTab1 = 621
    LimitedSecondDayTab2 = 622
    LimitedSecondDayTab3 = 623
    LimitedSecondDayTab4 = 624
    LimitedThirdDayTab1 = 631
    LimitedThirdDayTab2 = 632
    LimitedThirdDayTab3 = 633
    LimitedThirdDayTab4 = 634
    LimitedFourthDayTab1 = 641
    LimitedFourthDayTab2 = 642
    LimitedFourthDayTab3 = 643
    LimitedFourthDayTab4 = 644
    LimitedFifthDayTab1 = 651
    LimitedFifthDayTab2 = 652
    LimitedFifthDayTab3 = 653
    LimitedFifthDayTab4 = 654
    LimitedSixthDayTab1 = 661
    LimitedSixthDayTab2 = 662
    LimitedSixthDayTab3 = 663
    LimitedSixthDayTab4 = 664
    LimitedSeventhDayTab1 = 671
    LimitedSeventhDayTab2 = 672
    LimitedSeventhDayTab3 = 673
    LimitedSeventhDayTab4 = 674

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("解放されるコマンドの種類")]
class OpenCommandType(Enum):
    # [Description("コマンド無し")]
    None_ = 0
    # [Description("アルカナ")]
    Arcana = 1
    # [Description("ショップ")]
    Shop = 2
    # [Description("ミッション")]
    Mission = 3
    # [Description("時空の洞窟")]
    DungeonBattle = 4
    # [Description("バトルスキップ")]
    BattleSkip = 5
    # [Description("バトル倍速")]
    BattleSpeed = 6
    # [Description("バトル4倍速")]
    BattleSpeed4 = 7
    # [Description("時空の洞窟 見逃し補填")]
    DungeonBattleCompensation = 8
    # [Description("無窮の塔")]
    TowerBattle = 9
    # [Description("祈りの泉")]
    BountyQuest = 10
    # [Description("バトルリーグ")]
    BattleLeague = 11
    # [Description("幻影の神殿")]
    LocalRaid = 12
    # [Description("レジェンドリーグ")]
    LegendLeague = 13
    # [Description("運命ガチャ")]
    GachaDestiny = 14
    # [Description("エスペリアタワー")]
    EsperiaTower = 15
    # [Description("洞窟バトルハードモード")]
    DungeonBattleHardMode = 16
    # [Description("メモリー")]
    CharacterStory = 17
    # [Description("ロイヤルショップ")]
    RoyalShop = 18
    # [Description("ランキング")]
    Ranking = 19
    # [Description("スフィア装着")]
    SphereSet = 20
    # [Description("武具合成通常")]
    ShopNormalEquipment = 21
    # [Description("武具合成聖装")]
    ShopLegendEquipment = 22
    # [Description("ギルド（GVG）")]
    ShopGuild = 23
    # [Description("キャラコインショップ")]
    ShopCharacter = 24
    # [Description("時空の洞窟")]
    ShopDungeonBattle = 25
    # [Description("バトルリーグ")]
    ShopBattleLeague = 26
    # [Description("レジェンドリーグ")]
    ShopLegendLeague = 27
    # [Description("限定特典")]
    ShopLimited = 28
    # [Description("進化")]
    RankUp = 29
    # [Description("プレゼント")]
    Present = 30
    # [Description("武具強化")]
    EquipmentStrength = 31
    # [Description("神装強化")]
    EquipmentAscend = 32
    # [Description("武具進化")]
    EquipmentEvolution = 33
    # [Description("祈りの泉一括派遣、受け取り")]
    BountyQuestQuick = 34
    # [Description("ギルドレイドの掃討")]
    GuildRaidQuick = 35
    # [Description("ボス/無窮の塔掃討")]
    BossBattleQuick = 36
    # [Description("武具ガチャ")]
    GachaEquipment = 37
    # [Description("武具研磨")]
    EquipmentRefine = 38
    # [Description("フレンド")]
    Friend = 39
    # [Description("マイページ")]
    FooterMyPage = 40
    # [Description("キャラ")]
    FooterCharacter = 41
    # [Description("アイテムボックス")]
    FooterItemBox = 42
    # [Description("試練")]
    FooterCompetition = 43
    # [Description("ガチャ")]
    FooterGacha = 44
    # [Description("チャット")]
    FooterChat = 45
    # [Description("ギルド")]
    FooterGuild = 46
    # [Description("魔水晶（ショップ）&キャラ詳細_専用武器交換")]
    ShopMagicCrystal = 47
    # [Description("聖遺物（ショップ）")]
    ShopRelics = 48
    # [Description("スフィア（ショップ）")]
    ShopSphere = 49
    # [Description("イベント（ショップ）")]
    ShopEventExchange = 50
    # [Description("グランドバトル（ショップ）")]
    ShopGrandBattle = 51
    # [Description("レベルリンク")]
    LevelLink = 80
    # [Description("チュートリアルスキップ")]
    SkipTutorial = 100
    # [Description("月間ログインボーナス")]
    MonthlyLoginBonus = 120
    # [Description("期間限定ログインボーナス")]
    LimitedLoginBonus = 121
    # [Description("第二大陸")]
    SecondContinent = 140
    # [Description("フレンドコード")]
    FriendCode = 200

# [Description("ミッション達成条件タイプ")]
class MissionAchievementType(Enum):
    # [Description("無し")]
    None_ = 0
    # [Description("日付をまたいでログインした時")]
    Login = 100
    # [Description("ダイヤによる購入")]
    BoughtByCurrency = 200
    # [Description("フレンドコード使用")]
    UseFriendCode = 300
    # [Description("新キャラミッション")]
    NewCharacter = 1000
    # [Description("カムバックミッション中に貢献メダルを獲得した時")]
    MissionTotalActivityAtComeback = 1010100
    # [Description("新キャラミッション中に貢献メダルを獲得した時")]
    MissionTotalActivityAtNewCharacterMission = 1010200
    # [Description("期間限定ミッション中に貢献メダルを獲得した時")]
    MissionTotalActivityAtEvent = 1010300
    # [Description("マイページで自己紹介文を変更した時")]
    PlayerInfoEditComment = 2010100
    # [Description("フレンドになった最大の人数")]
    FriendMaxFriendCount = 3010100
    # [Description("フレンドポイントを送信した時")]
    FriendSendFriendPointCount = 3010200
    # [Description("アカウント連携を行った時")]
    SocialAuthAccount = 4010100
    # [Description("公式Twitterフォロー")]
    SocialFollowOfficialTwitter = 4020100
    # [Description("公式Youtubeフォロー")]
    SocialFollowOfficialYoutube = 4020200
    # [Description("ショップ（聖装鋼タブ）購入回数")]
    ExchangeLegendForgeMergeCount = 5010100
    # [Description("ショップ（精錬鋼タブ）購入回数")]
    ExchangeEquipmentForgeMergeCount = 5020200
    # [Description("ショップ（全てのタブ）購入回数")]
    ExchangeAllBuyCount = 5030100
    # [Description("ショップ（レギュラータブ）購入回数")]
    ExchangeRegularBuyCount = 5030200
    # [Description("ショップ（ギルドタブ）購入回数")]
    ExchangeGvGBuyCount = 5040100
    # [Description("ショップ（時空の洞窟タブ）購入回数")]
    ExchangeDungeonBattleBuyCount = 5050100
    # [Description("ロイヤルショップのダイヤ購入でダイヤを購入した時")]
    ShopTotalBuyCurrency = 6010100
    # [Description("キャラレベルアップ")]
    CharacterLevelUpCount = 7010100
    # [Description("レベルリンク達成レベル")]
    CharacterLevelLinkMaxLevel = 7010200
    # [Description("武具達成レベル")]
    CharacterEquipmentMaxLevel = 7010300
    # [Description("Lv1スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel1 = 7010401
    # [Description("Lv2スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel2 = 7010402
    # [Description("Lv3スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel3 = 7010403
    # [Description("Lv4スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel4 = 7010404
    # [Description("Lv5スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel5 = 7010405
    # [Description("Lv6スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel6 = 7010406
    # [Description("Lv7スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel7 = 7010407
    # [Description("Lv8スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel8 = 7010408
    # [Description("Lv9スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel9 = 7010409
    # [Description("魔装達成レベル")]
    CharacterMatchlessSacredTreasureMaxLevel = 7010500
    # [Description("聖装達成レベル")]
    CharacterLegendSacredTreasureMaxLevel = 7010600
    # [Description("武具研磨回数")]
    CharacterEquipmentTrainingCount = 7010700
    # [Description("武具強化達成レベル")]
    CharacterEquipmentReinforceMaxLevel = 7010800
    # [Description("神装強化回数")]
    CharacterEquipmentMergeCount = 7010900
    # [Description("最大総戦闘力")]
    CharacterMaxBattlePower = 7011000
    # [Description("キャラクター達成レベル")]
    CharacterCharacterMaxLevel = 7011100
    # [Description("武具強化最大達成レベル")]
    CharacterAllEquipmentReinforceMaxLevel = 7011200
    # [Description("キャラクター最高到達レアリティ")]
    CharacterRankUpMaxRarity = 7020100
    # [Description("キャラクター進化回数")]
    CharacterRankUpEvolutionCount = 7020200
    # [Description("レベルリンク枠解放数")]
    CharacterLevelLinkOpenSlotCount = 7030100
    # [Description("最高所持スフィアレベル")]
    EquipmentSphereMaxLevel = 8010100
    # [Description("スフィア合成回数")]
    EquipmentSphereComposeCount = 8010200
    # [Description("精錬武具（武具鋳造）個数")]
    EquipmentForgeCount = 8020100
    # [Description("Rナヘマー武具シリーズ合成回数")]
    EquipmentComposeCountR = 8030101
    # [Description("SRサンダルフォン武具シリーズ合成回数")]
    EquipmentComposeCountSR = 8030102
    # [Description("SSRアスタロト武具シリーズ合成回数")]
    EquipmentComposeCountSSR = 8030103
    # [Description("プレイヤー達成レベル")]
    AutoBattleMaxPlayerLevel = 9010100
    # [Description("獲得した合計領民数")]
    AutoBattleAddPopulation = 9010200
    # [Description("ボス勝利回数")]
    BossBattleVictoryCount = 9010300
    # [Description("最高到達クエスト")]
    AutoBattleMaxClearQuest = 9010400
    # [Description("最高到達章")]
    AutoBattledMaxClearChapter = 9010500
    # [Description("放置バトル報酬受け取り回数")]
    AutoBattleGetRewardCount = 9010600
    # [Description("高速バトル回数")]
    AutoBattleQuickCount = 9020100
    # [Description("時空の洞窟階層3クリア回数")]
    DungeonBattleClearThirdFloorCount = 10010100
    # [Description("時空の洞窟階層1クリア回数")]
    DungeonBattleClearFirstFloorCount = 10010200
    # [Description("時空の洞窟で〇人以上の○○タイプのキャラを使って戦闘に勝利")]
    DungeonBattleClearUnitJobTypeBase = 10010300
    # [Description("時空の洞窟で1人以上のウォリアータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear1UnitWarriorType = 10010311
    # [Description("時空の洞窟で1人以上のスナイパータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear1UnitSniperType = 10010312
    # [Description("時空の洞窟で1人以上のソーサラータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear1UnitSorcererType = 10010314
    # [Description("時空の洞窟で2人以上のウォリアータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear2UnitWarriorType = 10010321
    # [Description("時空の洞窟で2人以上のスナイパータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear2UnitSniperType = 10010322
    # [Description("時空の洞窟で2人以上のソーサラータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear2UnitSorcererType = 10010324
    # [Description("時空の洞窟で3人以上のウォリアータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear3UnitWarriorType = 10010331
    # [Description("時空の洞窟で3人以上のスナイパータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear3UnitSniperType = 10010332
    # [Description("時空の洞窟で3人以上のソーサラータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear3UnitSorcererType = 10010334
    # [Description("時空の洞窟で4人以上のウォリアータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear4UnitWarriorType = 10010341
    # [Description("時空の洞窟で4人以上のスナイパータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear4UnitSniperType = 10010342
    # [Description("時空の洞窟で4人以上のソーサラータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear4UnitSorcererType = 10010344
    # [Description("時空の洞窟で5人以上のウォリアータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear5UnitWarriorType = 10010351
    # [Description("時空の洞窟で5人以上のスナイパータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear5UnitSniperType = 10010352
    # [Description("時空の洞窟で5人以上のソーサラータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear5UnitSorcererType = 10010354
    # [Description("時空の洞窟新キャラミッション")]
    DungeonBattleNewCharacter = 10011000
    # [Description("無窮の塔階層クリア数")]
    TowerBattleMaxClearFloor = 11010100
    # [Description("属性の塔到達下限階層")]
    TowerBattleMinClearElementTower = 11010200
    # [Description("無窮の塔勝利回数")]
    TowerBattleTotalWinCount = 11010300
    # [Description("バトルリーグ挑戦回数")]
    BattleLeagueChallengeCount = 12010100
    # [Description("バトルリーグ最高順位")]
    BattleLeagueMaxRanking = 12010200
    # [Description("幻影の神殿勝利回数")]
    LocalRaidVictoryCount = 13010100
    # [Description("祈りの泉クエスト受領回数")]
    BountyQuestAllStartQuestCount = 14010100
    # [Description("祈りの泉新キャラミッション")]
    BountyQuestNewCharacter = 14011000
    # [Description("祈りの泉マルチクエスト受領回数")]
    BountyQuestTeamStartQuestCount = 14020100
    # [Description("キャラ入手数")]
    GachaNewJoinCharacter = 15010100
    # [Description("キャラガチャ回数")]
    GachaDrawCount = 15010200
    # [Description("ダイヤ消費量")]
    ConsumeCurrencyCount = 15010300
    # [Description("ギルド加入回数")]
    GuildJoinCount = 16010100
    # [Description("ギルドログイン回数")]
    GuildLoginCount = 16010200
    # [Description("ギルドレイド回数（解放ボス含む）")]
    GuildGuildRaidChallengeCount = 16020100
    # [Description("ワールドチャット発言回数")]
    ChatSayWorldChatCount = 17010100
    # [Description("アップデート回数")]
    OsStoreUpdateCount = 18010100

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("ミッション遷移先タイプ")]
class MissionTransitionDestinationType(Enum):
    # [Description("遷移先無し")]
    None_ = 0
    # [Description("デイリーミッション")]
    MissionDaily = 101
    # [Description("プレイヤー情報")]
    PlayerInfo = 201
    # [Description("フレンド一覧")]
    Friend = 301
    # [Description("アカウント連携")]
    LinkAccount = 401
    # [Description("Twitter ")]
    Twitter = 402
    # [Description("YouTube")]
    YouTube = 403
    # [Description("ショップ（武具合成＿聖装タブ）")]
    ExchangeLegendForge = 501
    # [Description("ショップ（武具合成＿通常タブ）")]
    ExchangeEquipmentForge = 502
    # [Description("ショップ（店舗タブ）")]
    Exchange = 503
    # [Description("GvGショップ")]
    ExchangeGvG = 504
    # [Description("時空の洞窟ショップ")]
    ExchangeDungeonBattle = 505
    # [Description("ロイヤルショップ＿ダイヤ購入タブ")]
    Shop = 601
    # [Description("キャラ画面（所持キャラタブ）")]
    CharacterList = 701
    # [Description("キャラ画面（進化タブ）")]
    CharacterRankUp = 702
    # [Description("レベルリンク（共鳴クリスタル）")]
    LevelLink = 703
    # [Description("アイテムボックス_スフィア")]
    ItemBoxSphere = 801
    # [Description("アイテムボックス_武具")]
    ItemBoxEquipment = 802
    # [Description("アイテムボックス画面（パーツタブ）")]
    ItemBoxParts = 803
    # [Description("オートバトル")]
    AutoBattle = 901
    # [Description("高速バトルダイアログ")]
    AutoBattleQuick = 902
    # [Description("時空の洞窟")]
    DungeonBattle = 1001
    # [Description("無窮の塔")]
    TowerBattle = 1101
    # [Description("バトルリーグ")]
    BattleLeague = 1201
    # [Description("幻影の神殿")]
    LocalRaid = 1301
    # [Description("祈りの泉（ノーマルタブ）")]
    BountyQuestSolo = 1401
    # [Description("祈りの泉（チームタブ）")]
    BountyQuestTeam = 1402
    # [Description("ガチャ（キャラタブ）")]
    Gacha = 1501
    # [Description("ギルド")]
    Guild = 1601
    # [Description("ギルドレイド画面（ソーニャ）")]
    GuildRaid = 1602
    # [Description("チャット")]
    Chat = 1701
    # [Description("各OSのストア")]
    OsStore = 1801
    # [Description("キャラ詳細")]
    CharacterDetail = 1901
    # [Description("マイページお気に入り設定ダイアログ")]
    FavoriteCharacter = 2001

# [MessagePackObject(True)]
@dataclass
class MissionReward():
    # [Nest(True, 1)]
    # [PropertyOrder(1)]
    Item: UserItem
    # [PropertyOrder(2)]
    RarityFlags: CharacterRarityFlags

# [Description("ミッションタイプ")]
class MissionType(Enum):
    Main = 0
    Daily = 1
    Weekly = 2
    BeginnerFirstDay = 311
    BeginnerFirstDayLevel = 312
    BeginnerFirstDayStage = 313
    BeginnerFirstDayBuy = 314
    BeginnerSecondDay = 321
    BeginnerSecondDayQuick = 322
    BeginnerSecondDayBattleLeague = 323
    BeginnerSecondDayBuy = 324
    BeginnerThirdDay = 331
    BeginnerThirdDayForge = 332
    BeginnerThirdDayDungeonBattle = 333
    BeginnerThirdDayBuy = 334
    BeginnerFourthDay = 341
    BeginnerFourthDayReinforceEquipment = 342
    BeginnerFourthDayTowerBattle = 343
    BeginnerFourthDayBuy = 344
    BeginnerFifthDay = 351
    BeginnerFifthDayBountyQuest = 352
    BeginnerFifthDayTotalCharacter = 353
    BeginnerFifthDayBuy = 354
    BeginnerSixthDay = 361
    BeginnerSixthDaySphere = 362
    BeginnerSixthDayCharacterEvolution = 363
    BeginnerSixthDayBuy = 364
    BeginnerSeventhDay = 371
    BeginnerSeventhDayTraining = 372
    BeginnerSeventhDayLocalRaid = 373
    BeginnerSeventhDayBuy = 374
    ComebackLogin = 401
    ComebackActivity = 402
    ComebackConsumeCurrency = 403
    NewCharacter = 5
    LimitedFirstDayTab1 = 611
    LimitedFirstDayTab2 = 612
    LimitedFirstDayTab3 = 613
    LimitedFirstDayTab4 = 614
    LimitedSecondDayTab1 = 621
    LimitedSecondDayTab2 = 622
    LimitedSecondDayTab3 = 623
    LimitedSecondDayTab4 = 624
    LimitedThirdDayTab1 = 631
    LimitedThirdDayTab2 = 632
    LimitedThirdDayTab3 = 633
    LimitedThirdDayTab4 = 634
    LimitedFourthDayTab1 = 641
    LimitedFourthDayTab2 = 642
    LimitedFourthDayTab3 = 643
    LimitedFourthDayTab4 = 644
    LimitedFifthDayTab1 = 651
    LimitedFifthDayTab2 = 652
    LimitedFifthDayTab3 = 653
    LimitedFifthDayTab4 = 654
    LimitedSixthDayTab1 = 661
    LimitedSixthDayTab2 = 662
    LimitedSixthDayTab3 = 663
    LimitedSixthDayTab4 = 664
    LimitedSeventhDayTab1 = 671
    LimitedSeventhDayTab2 = 672
    LimitedSeventhDayTab3 = 673
    LimitedSeventhDayTab4 = 674

# [Description("ミッション達成条件タイプ")]
class MissionAchievementType(Enum):
    # [Description("無し")]
    None_ = 0
    # [Description("日付をまたいでログインした時")]
    Login = 100
    # [Description("ダイヤによる購入")]
    BoughtByCurrency = 200
    # [Description("フレンドコード使用")]
    UseFriendCode = 300
    # [Description("新キャラミッション")]
    NewCharacter = 1000
    # [Description("カムバックミッション中に貢献メダルを獲得した時")]
    MissionTotalActivityAtComeback = 1010100
    # [Description("新キャラミッション中に貢献メダルを獲得した時")]
    MissionTotalActivityAtNewCharacterMission = 1010200
    # [Description("期間限定ミッション中に貢献メダルを獲得した時")]
    MissionTotalActivityAtEvent = 1010300
    # [Description("マイページで自己紹介文を変更した時")]
    PlayerInfoEditComment = 2010100
    # [Description("フレンドになった最大の人数")]
    FriendMaxFriendCount = 3010100
    # [Description("フレンドポイントを送信した時")]
    FriendSendFriendPointCount = 3010200
    # [Description("アカウント連携を行った時")]
    SocialAuthAccount = 4010100
    # [Description("公式Twitterフォロー")]
    SocialFollowOfficialTwitter = 4020100
    # [Description("公式Youtubeフォロー")]
    SocialFollowOfficialYoutube = 4020200
    # [Description("ショップ（聖装鋼タブ）購入回数")]
    ExchangeLegendForgeMergeCount = 5010100
    # [Description("ショップ（精錬鋼タブ）購入回数")]
    ExchangeEquipmentForgeMergeCount = 5020200
    # [Description("ショップ（全てのタブ）購入回数")]
    ExchangeAllBuyCount = 5030100
    # [Description("ショップ（レギュラータブ）購入回数")]
    ExchangeRegularBuyCount = 5030200
    # [Description("ショップ（ギルドタブ）購入回数")]
    ExchangeGvGBuyCount = 5040100
    # [Description("ショップ（時空の洞窟タブ）購入回数")]
    ExchangeDungeonBattleBuyCount = 5050100
    # [Description("ロイヤルショップのダイヤ購入でダイヤを購入した時")]
    ShopTotalBuyCurrency = 6010100
    # [Description("キャラレベルアップ")]
    CharacterLevelUpCount = 7010100
    # [Description("レベルリンク達成レベル")]
    CharacterLevelLinkMaxLevel = 7010200
    # [Description("武具達成レベル")]
    CharacterEquipmentMaxLevel = 7010300
    # [Description("Lv1スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel1 = 7010401
    # [Description("Lv2スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel2 = 7010402
    # [Description("Lv3スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel3 = 7010403
    # [Description("Lv4スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel4 = 7010404
    # [Description("Lv5スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel5 = 7010405
    # [Description("Lv6スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel6 = 7010406
    # [Description("Lv7スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel7 = 7010407
    # [Description("Lv8スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel8 = 7010408
    # [Description("Lv9スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel9 = 7010409
    # [Description("魔装達成レベル")]
    CharacterMatchlessSacredTreasureMaxLevel = 7010500
    # [Description("聖装達成レベル")]
    CharacterLegendSacredTreasureMaxLevel = 7010600
    # [Description("武具研磨回数")]
    CharacterEquipmentTrainingCount = 7010700
    # [Description("武具強化達成レベル")]
    CharacterEquipmentReinforceMaxLevel = 7010800
    # [Description("神装強化回数")]
    CharacterEquipmentMergeCount = 7010900
    # [Description("最大総戦闘力")]
    CharacterMaxBattlePower = 7011000
    # [Description("キャラクター達成レベル")]
    CharacterCharacterMaxLevel = 7011100
    # [Description("武具強化最大達成レベル")]
    CharacterAllEquipmentReinforceMaxLevel = 7011200
    # [Description("キャラクター最高到達レアリティ")]
    CharacterRankUpMaxRarity = 7020100
    # [Description("キャラクター進化回数")]
    CharacterRankUpEvolutionCount = 7020200
    # [Description("レベルリンク枠解放数")]
    CharacterLevelLinkOpenSlotCount = 7030100
    # [Description("最高所持スフィアレベル")]
    EquipmentSphereMaxLevel = 8010100
    # [Description("スフィア合成回数")]
    EquipmentSphereComposeCount = 8010200
    # [Description("精錬武具（武具鋳造）個数")]
    EquipmentForgeCount = 8020100
    # [Description("Rナヘマー武具シリーズ合成回数")]
    EquipmentComposeCountR = 8030101
    # [Description("SRサンダルフォン武具シリーズ合成回数")]
    EquipmentComposeCountSR = 8030102
    # [Description("SSRアスタロト武具シリーズ合成回数")]
    EquipmentComposeCountSSR = 8030103
    # [Description("プレイヤー達成レベル")]
    AutoBattleMaxPlayerLevel = 9010100
    # [Description("獲得した合計領民数")]
    AutoBattleAddPopulation = 9010200
    # [Description("ボス勝利回数")]
    BossBattleVictoryCount = 9010300
    # [Description("最高到達クエスト")]
    AutoBattleMaxClearQuest = 9010400
    # [Description("最高到達章")]
    AutoBattledMaxClearChapter = 9010500
    # [Description("放置バトル報酬受け取り回数")]
    AutoBattleGetRewardCount = 9010600
    # [Description("高速バトル回数")]
    AutoBattleQuickCount = 9020100
    # [Description("時空の洞窟階層3クリア回数")]
    DungeonBattleClearThirdFloorCount = 10010100
    # [Description("時空の洞窟階層1クリア回数")]
    DungeonBattleClearFirstFloorCount = 10010200
    # [Description("時空の洞窟で〇人以上の○○タイプのキャラを使って戦闘に勝利")]
    DungeonBattleClearUnitJobTypeBase = 10010300
    # [Description("時空の洞窟で1人以上のウォリアータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear1UnitWarriorType = 10010311
    # [Description("時空の洞窟で1人以上のスナイパータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear1UnitSniperType = 10010312
    # [Description("時空の洞窟で1人以上のソーサラータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear1UnitSorcererType = 10010314
    # [Description("時空の洞窟で2人以上のウォリアータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear2UnitWarriorType = 10010321
    # [Description("時空の洞窟で2人以上のスナイパータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear2UnitSniperType = 10010322
    # [Description("時空の洞窟で2人以上のソーサラータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear2UnitSorcererType = 10010324
    # [Description("時空の洞窟で3人以上のウォリアータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear3UnitWarriorType = 10010331
    # [Description("時空の洞窟で3人以上のスナイパータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear3UnitSniperType = 10010332
    # [Description("時空の洞窟で3人以上のソーサラータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear3UnitSorcererType = 10010334
    # [Description("時空の洞窟で4人以上のウォリアータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear4UnitWarriorType = 10010341
    # [Description("時空の洞窟で4人以上のスナイパータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear4UnitSniperType = 10010342
    # [Description("時空の洞窟で4人以上のソーサラータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear4UnitSorcererType = 10010344
    # [Description("時空の洞窟で5人以上のウォリアータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear5UnitWarriorType = 10010351
    # [Description("時空の洞窟で5人以上のスナイパータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear5UnitSniperType = 10010352
    # [Description("時空の洞窟で5人以上のソーサラータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear5UnitSorcererType = 10010354
    # [Description("時空の洞窟新キャラミッション")]
    DungeonBattleNewCharacter = 10011000
    # [Description("無窮の塔階層クリア数")]
    TowerBattleMaxClearFloor = 11010100
    # [Description("属性の塔到達下限階層")]
    TowerBattleMinClearElementTower = 11010200
    # [Description("無窮の塔勝利回数")]
    TowerBattleTotalWinCount = 11010300
    # [Description("バトルリーグ挑戦回数")]
    BattleLeagueChallengeCount = 12010100
    # [Description("バトルリーグ最高順位")]
    BattleLeagueMaxRanking = 12010200
    # [Description("幻影の神殿勝利回数")]
    LocalRaidVictoryCount = 13010100
    # [Description("祈りの泉クエスト受領回数")]
    BountyQuestAllStartQuestCount = 14010100
    # [Description("祈りの泉新キャラミッション")]
    BountyQuestNewCharacter = 14011000
    # [Description("祈りの泉マルチクエスト受領回数")]
    BountyQuestTeamStartQuestCount = 14020100
    # [Description("キャラ入手数")]
    GachaNewJoinCharacter = 15010100
    # [Description("キャラガチャ回数")]
    GachaDrawCount = 15010200
    # [Description("ダイヤ消費量")]
    ConsumeCurrencyCount = 15010300
    # [Description("ギルド加入回数")]
    GuildJoinCount = 16010100
    # [Description("ギルドログイン回数")]
    GuildLoginCount = 16010200
    # [Description("ギルドレイド回数（解放ボス含む）")]
    GuildGuildRaidChallengeCount = 16020100
    # [Description("ワールドチャット発言回数")]
    ChatSayWorldChatCount = 17010100
    # [Description("アップデート回数")]
    OsStoreUpdateCount = 18010100

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [MessagePackObject(True)]
@dataclass
class MissionReward():
    # [Nest(True, 1)]
    # [PropertyOrder(1)]
    Item: UserItem
    # [PropertyOrder(2)]
    RarityFlags: CharacterRarityFlags

# [Description("ミッショングループ")]
class MissionGroupType(Enum):
    # [Description("メイン")]
    Main = 0
    # [Description("デイリー")]
    Daily = 1
    # [Description("ウィークリー")]
    Weekly = 2
    # [Description("初心者")]
    Beginner = 3
    # [Description("カムバック")]
    Comeback = 4
    # [Description("新キャラ")]
    NewCharacter = 5
    # [Description("イベント")]
    Limited = 6

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [MessagePackObject(True)]
@dataclass
class LocalRaidQuestIdGroup():
    # [Description("幻影の神殿のクエストグループ種別")]
    # [PropertyOrder(1)]
    LocalRaidQuestGroupType: LocalRaidQuestGroupType
    # [Description("幻影の神殿のクエストIdグループ")]
    # [Nest(True, 1)]
    # [PropertyOrder(2)]
    LocalRaidQuestIdWeights: list[LocalRaidQuestIdWeight]

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [MessagePackObject(True)]
@dataclass
class LocalRaidStartEndTime():
    StartTime: int
    EndTime: int

class LocalRaidEventType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("クエスト追加イベント")]
    PlusQuest = 1
    # [Description("全日開催イベント")]
    FullOpen = 2

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("キャラクターのレアリティ")]
# [Flags]
class CharacterRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("N")]
    N = 1
    # [Description("R")]
    R = 2
    # [Description("R+")]
    RPlus = 4
    # [Description("SR")]
    SR = 8
    # [Description("SR+")]
    SRPlus = 16
    # [Description("SSR")]
    SSR = 32
    # [Description("SSR+")]
    SSRPlus = 64
    # [Description("UR")]
    UR = 128
    # [Description("UR+")]
    URPlus = 256
    # [Description("LR")]
    LR = 512
    # [Description("LR+")]
    LRPlus = 1024
    # [Description("LR+2")]
    LRPlus2 = 2048
    # [Description("LR+3")]
    LRPlus3 = 4096
    # [Description("LR+4")]
    LRPlus4 = 8192
    # [Description("LR+5")]
    LRPlus5 = 16384
    # [Description("LR+6")]
    LRPlus6 = 32768
    # [Description("LR+7")]
    LRPlus7 = 65536

class ElementType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("愁（しゅう）")]
    Blue = 1
    # [Description("業（ごう）")]
    Red = 2
    # [Description("心（しん）")]
    Green = 3
    # [Description("渇（かつ）")]
    Yellow = 4
    # [Description("天（てん） ")]
    Light = 5
    # [Description("冥（めい） ")]
    Dark = 6

# [Description("職業")]
# [Flags]
class JobFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("ウォリアー")]
    Warrior = 1
    # [Description("スナイパー")]
    Sniper = 2
    # [Description("ソーサラー")]
    Sorcerer = 4

# [Description("バトルパラメータ")]
# [MessagePackObject(True)]
@dataclass
class BattleParameter():
    # [Description("攻撃力")]
    AttackPower: int
    # [Description("回避")]
    Avoidance: int
    # [Description("クリティカル")]
    Critical: int
    # [Description("クリダメ強化")]
    CriticalDamageEnhance: int
    # [Description("クリティカル耐性")]
    CriticalResist: int
    # [Description("ダメージ強化")]
    DamageEnhance: int
    # [Description("カウンタ​")]
    DamageReflect: int
    # [Description("弱体効果命中​")]
    DebuffHit: int
    # [Description("弱体効果耐性")]
    DebuffResist: int
    # [Description("防御力")]
    Defense: int
    # [Description("防御貫通力")]
    DefensePenetration: int
    # [Description("命中")]
    Hit: int
    # [Description("HP")]
    HP: int
    # [Description("HP吸収")]
    HpDrain: int
    # [Description("魔法クリダメ緩和")]
    MagicCriticalDamageRelax: int
    # [Description("魔法ダメージ緩和")]
    MagicDamageRelax: int
    # [Description("物理クリダメ緩和")]
    PhysicalCriticalDamageRelax: int
    # [Description("物理ダメージ緩和")]
    PhysicalDamageRelax: int
    # [Description("スピード​")]
    Speed: int

class UnitIconType(Enum):
    # [Description("キャラクター")]
    Character = 0
    # [Description("敵キャラクター")]
    EnemyCharacter = 1
    # [Description("魔女クリファ")]
    WitchQlipha = 2

# [Description("基礎パラメータ")]
# [MessagePackObject(True)]
@dataclass
class BaseParameter():
    # [Description("技力​")]
    Energy: int
    # [Description("耐久力​")]
    Health: int
    # [Description("魔力")]
    Intelligence: int
    # [Description("筋力")]
    Muscle: int

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("ローカル通知種別")]
class LocalNotificationType(Enum):
    None_ = 0
    # [Description("オートバトル報酬上限到達")]
    AutoBattle = 1
    # [Description("幻影の神殿開始")]
    LocalRaid = 2
    # [Description("バトルリーグ報酬受け取り")]
    BattleLeagueReward = 3
    # [Description("幻影の神殿イベント報酬増加")]
    LocalRaidRewardIncrease = 4

# [Description("ローカル通知種別")]
class LocalNotificationSendType(Enum):
    None_ = 0
    # [Description("時刻指定")]
    TimeSpecified = 1
    # [Description("放置報酬上限到達")]
    AutoBattle = 2

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [Description("城タイプ")]
class CastleType(Enum):
    # [Description("下位")]
    Small = 0
    # [Description("中位")]
    Medium = 1
    # [Description("上位")]
    Large = 2

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("期間限定ログボの特別報酬アイテム")]
# [MessagePackObject(True)]
@dataclass
class SpecialLimitedLoginBonusItem():
    # [Description("日付")]
    # [PropertyOrder(1)]
    Date: int
    # [Description("特別報酬アイテム")]
    # [Nest(True, 1)]
    # [PropertyOrder(2)]
    SpecialRewardItem: UserItem
    # [Description("キャラレアリティ")]
    # [PropertyOrder(3)]
    RarityFlags: CharacterRarityFlags

# [Description("期間限定ログボの毎日報酬アイテム")]
# [MessagePackObject(True)]
@dataclass
class EveryDayLimitedLoginBonusItem():
    # [Description("毎日報酬アイテム")]
    # [Nest(True, 1)]
    # [PropertyOrder(1)]
    EveryDayRewardItem: UserItem
    # [Description("キャラレアリティ")]
    # [PropertyOrder(2)]
    RarityFlags: CharacterRarityFlags

# [Description("期間限定ログボの日別報酬アイテム")]
# [MessagePackObject(True)]
@dataclass
class DailyLimitedLoginBonusItem():
    # [Description("報酬アイテム")]
    # [Nest(True, 1)]
    # [PropertyOrder(2)]
    DailyRewardItem: UserItem
    # [Description("日付")]
    # [PropertyOrder(1)]
    Date: int
    # [Description("キャラレアリティ")]
    # [PropertyOrder(3)]
    RarityFlags: CharacterRarityFlags

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("期間限定イベントの種類")]
class LimitedEventType(Enum):
    # [Description("不明")]
    None_ = 0
    # [Description("属性の塔全開放")]
    ElementTowerAllRelease = 1
    # [Description("シリアルコード入力")]
    SerialCode = 2
    # [Description("古い課金システムの使用")]
    ApplyOldPurchaseSystem = 100

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("レジェンドリーグ階級の種類")]
class LegendLeagueClassType(Enum):
    None_ = 0
    # [Description("シュバリエ")]
    Chevalier = 1
    # [Description("パラディン")]
    Paladin = 2
    # [Description("デューク")]
    Duke = 3
    # [Description("ロイヤルランク")]
    Royal = 4
    # [Description("レジェンドランク")]
    Legend = 5
    # [Description("ワールド・ルーラー")]
    WorldRuler = 6

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("第2フレーム種類")]
class SecondaryFrameType(Enum):
    # [Description("不明")]
    None_ = 0
    # [Description("属性アイコン")]
    ElementIcon = 1
    # [Description("効果時間表示")]
    EffectTime = 2
    # [Description("レベル")]
    Level = 3
    # [Description("キャラアイコン_中央")]
    CenteredCharacterIcon = 4

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテムのレアリティ")]
# [Flags]
class ItemRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("D")]
    D = 1
    # [Description("C")]
    C = 2
    # [Description("B")]
    B = 4
    # [Description("A")]
    A = 8
    # [Description("S")]
    S = 16
    # [Description("R")]
    R = 32
    # [Description("SR")]
    SR = 64
    # [Description("SSR")]
    SSR = 128
    # [Description("UR")]
    UR = 256
    # [Description("LR")]
    LR = 512

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("各言語に翻訳されたテキスト")]
# [MessagePackObject(True)]
@dataclass
class TranslatedText():
    # [Description("英語")]
    # [PropertyOrder(2)]
    enUS: str
    # [Description("日本語")]
    # [PropertyOrder(1)]
    jaJP: str
    # [Description("韓国語")]
    # [PropertyOrder(3)]
    koKR: str
    # [Description("中国語(繁体字)")]
    # [PropertyOrder(4)]
    zhTW: str

# [Description("問い合わせボタンタイプ")]
class InquiryButtonType(Enum):
    # [Description("不明")]
    None_ = 0
    # [Description("URL")]
    Url = 1
    # [Description("メール")]
    Mail = 2
    # [Description("アカウント削除")]
    AccountDelete = 3

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("ヘルプパート")]
# [MessagePackObject(True)]
@dataclass
class HelpPartInfo():
    # [Description("見出し")]
    # [PropertyOrder(1)]
    HeadLine: str
    # [Description("本文")]
    # [PropertyOrder(2)]
    MainText: str
    # [Description("付加情報")]
    # [PropertyOrder(3)]
    HelpParameterType: HelpParameterType

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [MessagePackObject(True)]
@dataclass
class WorldDamageBarReward():
    GoalDamage: int
    # [Nest(True, 1)]
    WorldRewardItems: list[UserItem]

# [MessagePackObject(True)]
@dataclass
class GuildRaidQuestClearEquipmentLvList():
    EquipmentLv: int
    QuestClearValue: int

# [MessagePackObject(True)]
@dataclass
class NormalDamageBarReward():
    # [Nest(True, 1)]
    NormalRewardGoldCoefficientInfo: GuildRaidGoldCoefficientInfo
    DamageBarCount: int
    # [Nest(True, 1)]
    NormalRewardItems: list[UserItem]

# [MessagePackObject(True)]
@dataclass
class GuildDamageBarReward():
    DamageBarCount: int
    # [Nest(True, 1)]
    GuildRewardItems: list[UserItem]

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

class UnitIconType(Enum):
    # [Description("キャラクター")]
    Character = 0
    # [Description("敵キャラクター")]
    EnemyCharacter = 1
    # [Description("魔女クリファ")]
    WitchQlipha = 2

# [MessagePackObject(True)]
@dataclass
class GuildRaidDamageBar():
    DamageBarCount: int
    DamageBarMaxValue: int

# [Description("職業")]
# [Flags]
class JobFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("ウォリアー")]
    Warrior = 1
    # [Description("スナイパー")]
    Sniper = 2
    # [Description("ソーサラー")]
    Sorcerer = 4

class GuildRaidBossType(Enum):
    # [Description("通常ボス")]
    Normal = 0
    # [Description("解放ボス")]
    Releasable = 1
    # [Description("イベントボス")]
    Event = 2

# [MessagePackObject(True)]
@dataclass
class GuildRaidDamageBar():
    DamageBarCount: int
    DamageBarMaxValue: int

class ElementType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("愁（しゅう）")]
    Blue = 1
    # [Description("業（ごう）")]
    Red = 2
    # [Description("心（しん）")]
    Green = 3
    # [Description("渇（かつ）")]
    Yellow = 4
    # [Description("天（てん） ")]
    Light = 5
    # [Description("冥（めい） ")]
    Dark = 6

# [Description("キャラクターのレアリティ")]
# [Flags]
class CharacterRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("N")]
    N = 1
    # [Description("R")]
    R = 2
    # [Description("R+")]
    RPlus = 4
    # [Description("SR")]
    SR = 8
    # [Description("SR+")]
    SRPlus = 16
    # [Description("SSR")]
    SSR = 32
    # [Description("SSR+")]
    SSRPlus = 64
    # [Description("UR")]
    UR = 128
    # [Description("UR+")]
    URPlus = 256
    # [Description("LR")]
    LR = 512
    # [Description("LR+")]
    LRPlus = 1024
    # [Description("LR+2")]
    LRPlus2 = 2048
    # [Description("LR+3")]
    LRPlus3 = 4096
    # [Description("LR+4")]
    LRPlus4 = 8192
    # [Description("LR+5")]
    LRPlus5 = 16384
    # [Description("LR+6")]
    LRPlus6 = 32768
    # [Description("LR+7")]
    LRPlus7 = 65536

# [Description("バトルパラメータ")]
# [MessagePackObject(True)]
@dataclass
class BattleParameter():
    # [Description("攻撃力")]
    AttackPower: int
    # [Description("回避")]
    Avoidance: int
    # [Description("クリティカル")]
    Critical: int
    # [Description("クリダメ強化")]
    CriticalDamageEnhance: int
    # [Description("クリティカル耐性")]
    CriticalResist: int
    # [Description("ダメージ強化")]
    DamageEnhance: int
    # [Description("カウンタ​")]
    DamageReflect: int
    # [Description("弱体効果命中​")]
    DebuffHit: int
    # [Description("弱体効果耐性")]
    DebuffResist: int
    # [Description("防御力")]
    Defense: int
    # [Description("防御貫通力")]
    DefensePenetration: int
    # [Description("命中")]
    Hit: int
    # [Description("HP")]
    HP: int
    # [Description("HP吸収")]
    HpDrain: int
    # [Description("魔法クリダメ緩和")]
    MagicCriticalDamageRelax: int
    # [Description("魔法ダメージ緩和")]
    MagicDamageRelax: int
    # [Description("物理クリダメ緩和")]
    PhysicalCriticalDamageRelax: int
    # [Description("物理ダメージ緩和")]
    PhysicalDamageRelax: int
    # [Description("スピード​")]
    Speed: int

# [Description("基礎パラメータ")]
# [MessagePackObject(True)]
@dataclass
class BaseParameter():
    # [Description("技力​")]
    Energy: int
    # [Description("耐久力​")]
    Health: int
    # [Description("魔力")]
    Intelligence: int
    # [Description("筋力")]
    Muscle: int

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [MessagePackObject(True)]
@dataclass
class GlobalGvgFixedRewards():
    # [Nest(True, 1)]
    LowerClass: list[UserItem]
    # [Nest(True, 1)]
    MediumClass: list[UserItem]
    # [Nest(True, 1)]
    UpperClass: list[UserItem]

# [Description("城タイプ")]
class CastleType(Enum):
    # [Description("下位")]
    Small = 0
    # [Description("中位")]
    Medium = 1
    # [Description("上位")]
    Large = 2

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("ガチャセレクトリストタイプ")]
class GachaSelectListType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("プライズ共通")]
    Default = 1
    # [Description("運命")]
    Destiny = 2

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("ガチャ追加キャラタイプ")]
class GachaAddCharacterType(Enum):
    # [Description("未指定")]
    None_ = 0
    # [Description("復刻")]
    Reprint = 1
    # [Description("新規")]
    New = 2

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [Description("タイトル背景色")]
class GachaTitleColorType(Enum):
    None_ = 0
    # [Description("黄色")]
    Yellow = 1
    # [Description("緑")]
    Green = 2
    # [Description("青")]
    Blue = 3
    # [Description("赤紫")]
    RedPurple = 4
    # [Description("水灰")]
    BlueGray = 5
    # [Description("青紫")]
    BluePurple = 6
    # [Description("赤")]
    Red = 7

# [Description("各言語に翻訳されたテキスト")]
# [MessagePackObject(True)]
@dataclass
class TranslatedText():
    # [Description("英語")]
    # [PropertyOrder(2)]
    enUS: str
    # [Description("日本語")]
    # [PropertyOrder(1)]
    jaJP: str
    # [Description("韓国語")]
    # [PropertyOrder(3)]
    koKR: str
    # [Description("中国語(繁体字)")]
    # [PropertyOrder(4)]
    zhTW: str

# [Description("各言語に翻訳されたテキスト")]
# [MessagePackObject(True)]
@dataclass
class TranslatedText():
    # [Description("英語")]
    # [PropertyOrder(2)]
    enUS: str
    # [Description("日本語")]
    # [PropertyOrder(1)]
    jaJP: str
    # [Description("韓国語")]
    # [PropertyOrder(3)]
    koKR: str
    # [Description("中国語(繁体字)")]
    # [PropertyOrder(4)]
    zhTW: str

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [Description("各言語に翻訳されたテキスト")]
# [MessagePackObject(True)]
@dataclass
class TranslatedText():
    # [Description("英語")]
    # [PropertyOrder(2)]
    enUS: str
    # [Description("日本語")]
    # [PropertyOrder(1)]
    jaJP: str
    # [Description("韓国語")]
    # [PropertyOrder(3)]
    koKR: str
    # [Description("中国語(繁体字)")]
    # [PropertyOrder(4)]
    zhTW: str

# [Description("ガチャボーナスゲージ表示タイプ")]
class GachaBonusGaugeType(Enum):
    # [Description("次のボーナスでドローカウントをリセット")]
    SingleReset = 0
    # [Description("ドロー回数を累計表示")]
    SingleSum = 1
    # [Description("ボーナスを複数表示")]
    Multi = 2

# [Description("各言語に翻訳されたテキスト")]
# [MessagePackObject(True)]
@dataclass
class TranslatedText():
    # [Description("英語")]
    # [PropertyOrder(2)]
    enUS: str
    # [Description("日本語")]
    # [PropertyOrder(1)]
    jaJP: str
    # [Description("韓国語")]
    # [PropertyOrder(3)]
    koKR: str
    # [Description("中国語(繁体字)")]
    # [PropertyOrder(4)]
    zhTW: str

# [Description("各言語に翻訳されたテキスト")]
# [MessagePackObject(True)]
@dataclass
class TranslatedText():
    # [Description("英語")]
    # [PropertyOrder(2)]
    enUS: str
    # [Description("日本語")]
    # [PropertyOrder(1)]
    jaJP: str
    # [Description("韓国語")]
    # [PropertyOrder(3)]
    koKR: str
    # [Description("中国語(繁体字)")]
    # [PropertyOrder(4)]
    zhTW: str

# [Description("各言語に翻訳されたテキスト")]
# [MessagePackObject(True)]
@dataclass
class TranslatedText():
    # [Description("英語")]
    # [PropertyOrder(2)]
    enUS: str
    # [Description("日本語")]
    # [PropertyOrder(1)]
    jaJP: str
    # [Description("韓国語")]
    # [PropertyOrder(3)]
    koKR: str
    # [Description("中国語(繁体字)")]
    # [PropertyOrder(4)]
    zhTW: str

# [Description("各言語に翻訳されたテキスト")]
# [MessagePackObject(True)]
@dataclass
class TranslatedText():
    # [Description("英語")]
    # [PropertyOrder(2)]
    enUS: str
    # [Description("日本語")]
    # [PropertyOrder(1)]
    jaJP: str
    # [Description("韓国語")]
    # [PropertyOrder(3)]
    koKR: str
    # [Description("中国語(繁体字)")]
    # [PropertyOrder(4)]
    zhTW: str

# [Description("各言語に翻訳されたテキスト")]
# [MessagePackObject(True)]
@dataclass
class TranslatedText():
    # [Description("英語")]
    # [PropertyOrder(2)]
    enUS: str
    # [Description("日本語")]
    # [PropertyOrder(1)]
    jaJP: str
    # [Description("韓国語")]
    # [PropertyOrder(3)]
    koKR: str
    # [Description("中国語(繁体字)")]
    # [PropertyOrder(4)]
    zhTW: str

# [MessagePackObject(True)]
@dataclass
class CustomTextLayout():
    # [Description("英語")]
    # [Nest(True, 2)]
    # [PropertyOrder(2)]
    enUS: CustomTextLayoutInfo
    # [Description("日本語")]
    # [Nest(True, 2)]
    # [PropertyOrder(1)]
    jaJP: CustomTextLayoutInfo
    # [Description("韓国語")]
    # [Nest(True, 2)]
    # [PropertyOrder(3)]
    koKR: CustomTextLayoutInfo
    # [Description("中国語(繁体字)")]
    # [Nest(True, 2)]
    # [PropertyOrder(5)]
    zhTW: CustomTextLayoutInfo

# [Description("各言語に翻訳されたテキスト")]
# [MessagePackObject(True)]
@dataclass
class TranslatedText():
    # [Description("英語")]
    # [PropertyOrder(2)]
    enUS: str
    # [Description("日本語")]
    # [PropertyOrder(1)]
    jaJP: str
    # [Description("韓国語")]
    # [PropertyOrder(3)]
    koKR: str
    # [Description("中国語(繁体字)")]
    # [PropertyOrder(4)]
    zhTW: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("ガチャ表示用フラグ")]
# [Flags]
class GachaCaseFlags(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("天井表示")]
    ShowCeilingCount = 1
    # [Description("レビュー誘導判定無し")]
    IgnoreReview = 2
    # [Description("シェアボタン表示なし")]
    HideShareButton = 4
    # [Description("ガチャ詳細ダイアログ スペシャルリスト非表示")]
    HideSpecialList = 8

# [Description("ガチャセレクトリストタイプ")]
class GachaSelectListType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("プライズ共通")]
    Default = 1
    # [Description("運命")]
    Destiny = 2

# [Description("ガチャリセットタイプ")]
class GachaResetType(Enum):
    # [Description("リセット無し")]
    None_ = 0
    # [Description("毎日4:00")]
    Daily = 1
    # [Description("毎週月曜4:00")]
    Weekly = 2

# [Description("ガチャ聖遺物タイプ")]
class GachaRelicType(Enum):
    None_ = 0
    # [Description("天契の聖杯")]
    ChaliceOfHeavenly = 1
    # [Description("蒼穹の銀勲")]
    SilverOrderOfTheBlueSky = 2
    # [Description("希求の神翼")]
    DivineWingsOfDesire = 3
    # [Description("悠園の果実")]
    FruitOfTheGarden = 4

# [Description("ガチャグループタイプ")]
class GachaGroupType(Enum):
    # [Description("グループ無し")]
    None_ = 0
    # [Description("属性")]
    Element = 1
    # [Description("聖天使の神託")]
    HolyAngel = 2

# [Description("運命ガチャタイプ")]
class GachaDestinyType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("愁、業、心、渇属性")]
    BlueAndRedAndGreenAndYellow = 1
    # [Description("こちらの承認")]
    LightAndDark = 2

# [Description("ガチャカテゴリータイプ")]
class GachaCategoryType(Enum):
    # [Description("キャラ")]
    Character = 0
    # [Description("武具")]
    Equipment = 1

class ElementType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("愁（しゅう）")]
    Blue = 1
    # [Description("業（ごう）")]
    Red = 2
    # [Description("心（しん）")]
    Green = 3
    # [Description("渇（かつ）")]
    Yellow = 4
    # [Description("天（てん） ")]
    Light = 5
    # [Description("冥（めい） ")]
    Dark = 6

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [Description("ミッション達成条件タイプ")]
class MissionAchievementType(Enum):
    # [Description("無し")]
    None_ = 0
    # [Description("日付をまたいでログインした時")]
    Login = 100
    # [Description("ダイヤによる購入")]
    BoughtByCurrency = 200
    # [Description("フレンドコード使用")]
    UseFriendCode = 300
    # [Description("新キャラミッション")]
    NewCharacter = 1000
    # [Description("カムバックミッション中に貢献メダルを獲得した時")]
    MissionTotalActivityAtComeback = 1010100
    # [Description("新キャラミッション中に貢献メダルを獲得した時")]
    MissionTotalActivityAtNewCharacterMission = 1010200
    # [Description("期間限定ミッション中に貢献メダルを獲得した時")]
    MissionTotalActivityAtEvent = 1010300
    # [Description("マイページで自己紹介文を変更した時")]
    PlayerInfoEditComment = 2010100
    # [Description("フレンドになった最大の人数")]
    FriendMaxFriendCount = 3010100
    # [Description("フレンドポイントを送信した時")]
    FriendSendFriendPointCount = 3010200
    # [Description("アカウント連携を行った時")]
    SocialAuthAccount = 4010100
    # [Description("公式Twitterフォロー")]
    SocialFollowOfficialTwitter = 4020100
    # [Description("公式Youtubeフォロー")]
    SocialFollowOfficialYoutube = 4020200
    # [Description("ショップ（聖装鋼タブ）購入回数")]
    ExchangeLegendForgeMergeCount = 5010100
    # [Description("ショップ（精錬鋼タブ）購入回数")]
    ExchangeEquipmentForgeMergeCount = 5020200
    # [Description("ショップ（全てのタブ）購入回数")]
    ExchangeAllBuyCount = 5030100
    # [Description("ショップ（レギュラータブ）購入回数")]
    ExchangeRegularBuyCount = 5030200
    # [Description("ショップ（ギルドタブ）購入回数")]
    ExchangeGvGBuyCount = 5040100
    # [Description("ショップ（時空の洞窟タブ）購入回数")]
    ExchangeDungeonBattleBuyCount = 5050100
    # [Description("ロイヤルショップのダイヤ購入でダイヤを購入した時")]
    ShopTotalBuyCurrency = 6010100
    # [Description("キャラレベルアップ")]
    CharacterLevelUpCount = 7010100
    # [Description("レベルリンク達成レベル")]
    CharacterLevelLinkMaxLevel = 7010200
    # [Description("武具達成レベル")]
    CharacterEquipmentMaxLevel = 7010300
    # [Description("Lv1スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel1 = 7010401
    # [Description("Lv2スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel2 = 7010402
    # [Description("Lv3スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel3 = 7010403
    # [Description("Lv4スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel4 = 7010404
    # [Description("Lv5スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel5 = 7010405
    # [Description("Lv6スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel6 = 7010406
    # [Description("Lv7スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel7 = 7010407
    # [Description("Lv8スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel8 = 7010408
    # [Description("Lv9スフィア装着個数")]
    CharacterSphereMaxEquipCountLevel9 = 7010409
    # [Description("魔装達成レベル")]
    CharacterMatchlessSacredTreasureMaxLevel = 7010500
    # [Description("聖装達成レベル")]
    CharacterLegendSacredTreasureMaxLevel = 7010600
    # [Description("武具研磨回数")]
    CharacterEquipmentTrainingCount = 7010700
    # [Description("武具強化達成レベル")]
    CharacterEquipmentReinforceMaxLevel = 7010800
    # [Description("神装強化回数")]
    CharacterEquipmentMergeCount = 7010900
    # [Description("最大総戦闘力")]
    CharacterMaxBattlePower = 7011000
    # [Description("キャラクター達成レベル")]
    CharacterCharacterMaxLevel = 7011100
    # [Description("武具強化最大達成レベル")]
    CharacterAllEquipmentReinforceMaxLevel = 7011200
    # [Description("キャラクター最高到達レアリティ")]
    CharacterRankUpMaxRarity = 7020100
    # [Description("キャラクター進化回数")]
    CharacterRankUpEvolutionCount = 7020200
    # [Description("レベルリンク枠解放数")]
    CharacterLevelLinkOpenSlotCount = 7030100
    # [Description("最高所持スフィアレベル")]
    EquipmentSphereMaxLevel = 8010100
    # [Description("スフィア合成回数")]
    EquipmentSphereComposeCount = 8010200
    # [Description("精錬武具（武具鋳造）個数")]
    EquipmentForgeCount = 8020100
    # [Description("Rナヘマー武具シリーズ合成回数")]
    EquipmentComposeCountR = 8030101
    # [Description("SRサンダルフォン武具シリーズ合成回数")]
    EquipmentComposeCountSR = 8030102
    # [Description("SSRアスタロト武具シリーズ合成回数")]
    EquipmentComposeCountSSR = 8030103
    # [Description("プレイヤー達成レベル")]
    AutoBattleMaxPlayerLevel = 9010100
    # [Description("獲得した合計領民数")]
    AutoBattleAddPopulation = 9010200
    # [Description("ボス勝利回数")]
    BossBattleVictoryCount = 9010300
    # [Description("最高到達クエスト")]
    AutoBattleMaxClearQuest = 9010400
    # [Description("最高到達章")]
    AutoBattledMaxClearChapter = 9010500
    # [Description("放置バトル報酬受け取り回数")]
    AutoBattleGetRewardCount = 9010600
    # [Description("高速バトル回数")]
    AutoBattleQuickCount = 9020100
    # [Description("時空の洞窟階層3クリア回数")]
    DungeonBattleClearThirdFloorCount = 10010100
    # [Description("時空の洞窟階層1クリア回数")]
    DungeonBattleClearFirstFloorCount = 10010200
    # [Description("時空の洞窟で〇人以上の○○タイプのキャラを使って戦闘に勝利")]
    DungeonBattleClearUnitJobTypeBase = 10010300
    # [Description("時空の洞窟で1人以上のウォリアータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear1UnitWarriorType = 10010311
    # [Description("時空の洞窟で1人以上のスナイパータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear1UnitSniperType = 10010312
    # [Description("時空の洞窟で1人以上のソーサラータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear1UnitSorcererType = 10010314
    # [Description("時空の洞窟で2人以上のウォリアータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear2UnitWarriorType = 10010321
    # [Description("時空の洞窟で2人以上のスナイパータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear2UnitSniperType = 10010322
    # [Description("時空の洞窟で2人以上のソーサラータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear2UnitSorcererType = 10010324
    # [Description("時空の洞窟で3人以上のウォリアータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear3UnitWarriorType = 10010331
    # [Description("時空の洞窟で3人以上のスナイパータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear3UnitSniperType = 10010332
    # [Description("時空の洞窟で3人以上のソーサラータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear3UnitSorcererType = 10010334
    # [Description("時空の洞窟で4人以上のウォリアータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear4UnitWarriorType = 10010341
    # [Description("時空の洞窟で4人以上のスナイパータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear4UnitSniperType = 10010342
    # [Description("時空の洞窟で4人以上のソーサラータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear4UnitSorcererType = 10010344
    # [Description("時空の洞窟で5人以上のウォリアータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear5UnitWarriorType = 10010351
    # [Description("時空の洞窟で5人以上のスナイパータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear5UnitSniperType = 10010352
    # [Description("時空の洞窟で5人以上のソーサラータイプのキャラを使って戦闘に勝利")]
    DungeonBattleClear5UnitSorcererType = 10010354
    # [Description("時空の洞窟新キャラミッション")]
    DungeonBattleNewCharacter = 10011000
    # [Description("無窮の塔階層クリア数")]
    TowerBattleMaxClearFloor = 11010100
    # [Description("属性の塔到達下限階層")]
    TowerBattleMinClearElementTower = 11010200
    # [Description("無窮の塔勝利回数")]
    TowerBattleTotalWinCount = 11010300
    # [Description("バトルリーグ挑戦回数")]
    BattleLeagueChallengeCount = 12010100
    # [Description("バトルリーグ最高順位")]
    BattleLeagueMaxRanking = 12010200
    # [Description("幻影の神殿勝利回数")]
    LocalRaidVictoryCount = 13010100
    # [Description("祈りの泉クエスト受領回数")]
    BountyQuestAllStartQuestCount = 14010100
    # [Description("祈りの泉新キャラミッション")]
    BountyQuestNewCharacter = 14011000
    # [Description("祈りの泉マルチクエスト受領回数")]
    BountyQuestTeamStartQuestCount = 14020100
    # [Description("キャラ入手数")]
    GachaNewJoinCharacter = 15010100
    # [Description("キャラガチャ回数")]
    GachaDrawCount = 15010200
    # [Description("ダイヤ消費量")]
    ConsumeCurrencyCount = 15010300
    # [Description("ギルド加入回数")]
    GuildJoinCount = 16010100
    # [Description("ギルドログイン回数")]
    GuildLoginCount = 16010200
    # [Description("ギルドレイド回数（解放ボス含む）")]
    GuildGuildRaidChallengeCount = 16020100
    # [Description("ワールドチャット発言回数")]
    ChatSayWorldChatCount = 17010100
    # [Description("アップデート回数")]
    OsStoreUpdateCount = 18010100

# [Description("ミッション遷移先タイプ")]
class MissionTransitionDestinationType(Enum):
    # [Description("遷移先無し")]
    None_ = 0
    # [Description("デイリーミッション")]
    MissionDaily = 101
    # [Description("プレイヤー情報")]
    PlayerInfo = 201
    # [Description("フレンド一覧")]
    Friend = 301
    # [Description("アカウント連携")]
    LinkAccount = 401
    # [Description("Twitter ")]
    Twitter = 402
    # [Description("YouTube")]
    YouTube = 403
    # [Description("ショップ（武具合成＿聖装タブ）")]
    ExchangeLegendForge = 501
    # [Description("ショップ（武具合成＿通常タブ）")]
    ExchangeEquipmentForge = 502
    # [Description("ショップ（店舗タブ）")]
    Exchange = 503
    # [Description("GvGショップ")]
    ExchangeGvG = 504
    # [Description("時空の洞窟ショップ")]
    ExchangeDungeonBattle = 505
    # [Description("ロイヤルショップ＿ダイヤ購入タブ")]
    Shop = 601
    # [Description("キャラ画面（所持キャラタブ）")]
    CharacterList = 701
    # [Description("キャラ画面（進化タブ）")]
    CharacterRankUp = 702
    # [Description("レベルリンク（共鳴クリスタル）")]
    LevelLink = 703
    # [Description("アイテムボックス_スフィア")]
    ItemBoxSphere = 801
    # [Description("アイテムボックス_武具")]
    ItemBoxEquipment = 802
    # [Description("アイテムボックス画面（パーツタブ）")]
    ItemBoxParts = 803
    # [Description("オートバトル")]
    AutoBattle = 901
    # [Description("高速バトルダイアログ")]
    AutoBattleQuick = 902
    # [Description("時空の洞窟")]
    DungeonBattle = 1001
    # [Description("無窮の塔")]
    TowerBattle = 1101
    # [Description("バトルリーグ")]
    BattleLeague = 1201
    # [Description("幻影の神殿")]
    LocalRaid = 1301
    # [Description("祈りの泉（ノーマルタブ）")]
    BountyQuestSolo = 1401
    # [Description("祈りの泉（チームタブ）")]
    BountyQuestTeam = 1402
    # [Description("ガチャ（キャラタブ）")]
    Gacha = 1501
    # [Description("ギルド")]
    Guild = 1601
    # [Description("ギルドレイド画面（ソーニャ）")]
    GuildRaid = 1602
    # [Description("チャット")]
    Chat = 1701
    # [Description("各OSのストア")]
    OsStore = 1801
    # [Description("キャラ詳細")]
    CharacterDetail = 1901
    # [Description("マイページお気に入り設定ダイアログ")]
    FavoriteCharacter = 2001

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("各言語に翻訳されたテキスト")]
# [MessagePackObject(True)]
@dataclass
class TranslatedText():
    # [Description("英語")]
    # [PropertyOrder(2)]
    enUS: str
    # [Description("日本語")]
    # [PropertyOrder(1)]
    jaJP: str
    # [Description("韓国語")]
    # [PropertyOrder(3)]
    koKR: str
    # [Description("中国語(繁体字)")]
    # [PropertyOrder(4)]
    zhTW: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

class ErrorMessageType(Enum):
    None_ = 0
    Dialog = 1
    DialogWithError = 2
    Toast = 3

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("セット装備の効果")]
# [MessagePackObject(True)]
@dataclass
class EquipmentSetEffect():
    # [Description("発動効果(BaseParameter)")]
    # [Nest(True, 1)]
    # [PropertyOrder(2)]
    BaseParameterChangeInfo: BaseParameterChangeInfo
    # [Description("発動効果(BattleParameter)")]
    # [Nest(True, 1)]
    # [PropertyOrder(3)]
    BattleParameterChangeInfo: BattleParameterChangeInfo
    # [Description("発動に必要な装備数")]
    # [PropertyOrder(1)]
    RequiredEquipmentCount: int

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("アイテムのレアリティ")]
# [Flags]
class ItemRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("D")]
    D = 1
    # [Description("C")]
    C = 2
    # [Description("B")]
    B = 4
    # [Description("A")]
    A = 8
    # [Description("S")]
    S = 16
    # [Description("R")]
    R = 32
    # [Description("SR")]
    SR = 64
    # [Description("SSR")]
    SSR = 128
    # [Description("UR")]
    UR = 256
    # [Description("LR")]
    LR = 512

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("武具強化必要アイテム情報")]
# [MessagePackObject(True)]
@dataclass
class EquipmentReinforcementMaterialInfo():
    # [Description("レベル")]
    # [PropertyOrder(1)]
    Lv: int
    # [Description("必要アイテム")]
    # [Nest(True, 1)]
    # [PropertyOrder(2)]
    RequiredItemList: list[UserItem]

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("武具の種類")]
class EquipmentSlotType(Enum):
    # [Description("武器")]
    Weapon = 1
    # [Description("装飾品")]
    Sub = 2
    # [Description("アーム")]
    Gauntlet = 3
    # [Description("メット")]
    Helmet = 4
    # [Description("メイル")]
    Armor = 5
    # [Description("ブーツ")]
    Shoes = 6

# [Description("武具のレアリティ")]
# [Flags]
class EquipmentRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("D")]
    D = 1
    # [Description("C")]
    C = 2
    # [Description("B")]
    B = 4
    # [Description("A")]
    A = 8
    # [Description("S")]
    S = 16
    # [Description("R")]
    R = 32
    # [Description("SR")]
    SR = 64
    # [Description("SSR")]
    SSR = 128
    # [Description("UR")]
    UR = 256
    # [Description("LR")]
    LR = 512

# [Description("職業")]
# [Flags]
class JobFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("ウォリアー")]
    Warrior = 1
    # [Description("スナイパー")]
    Sniper = 2
    # [Description("ソーサラー")]
    Sorcerer = 4

# [Description("武具カテゴリ")]
class EquipmentCategory(Enum):
    # [Description("通常武具")]
    Normal = 1
    # [Description("セット武具")]
    Set = 2
    # [Description("専用武器")]
    Exclusive = 3

# [Description("バトルパラメータ変動情報")]
# [MessagePackObject(True)]
@dataclass
class BattleParameterChangeInfo():
    # [Description("変動するバトルパラメータ")]
    # [PropertyOrder(1)]
    BattleParameterType: BattleParameterType
    # [Description("パラメータ増減タイプ")]
    # [PropertyOrder(2)]
    ChangeParameterType: ChangeParameterType
    # [Description("値")]
    # [PropertyOrder(3)]
    Value: float

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("武具のレアリティ")]
# [Flags]
class EquipmentRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("D")]
    D = 1
    # [Description("C")]
    C = 2
    # [Description("B")]
    B = 4
    # [Description("A")]
    A = 8
    # [Description("S")]
    S = 16
    # [Description("R")]
    R = 32
    # [Description("SR")]
    SR = 64
    # [Description("SSR")]
    SSR = 128
    # [Description("UR")]
    UR = 256
    # [Description("LR")]
    LR = 512

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("バトルパラメータ変動情報")]
# [MessagePackObject(True)]
@dataclass
class BattleParameterChangeInfo():
    # [Description("変動するバトルパラメータ")]
    # [PropertyOrder(1)]
    BattleParameterType: BattleParameterType
    # [Description("パラメータ増減タイプ")]
    # [PropertyOrder(2)]
    ChangeParameterType: ChangeParameterType
    # [Description("値")]
    # [PropertyOrder(3)]
    Value: float

# [Description("基礎パラメータ変動情報")]
# [MessagePackObject(True)]
@dataclass
class BaseParameterChangeInfo():
    # [Description("変動する基礎パラメータ")]
    # [PropertyOrder(1)]
    BaseParameterType: BaseParameterType
    # [Description("パラメータ増減タイプ")]
    # [PropertyOrder(2)]
    ChangeParameterType: ChangeParameterType
    # [Description("値")]
    # [PropertyOrder(3)]
    Value: float

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("武具進化の種類")]
class EvolutionType(Enum):
    # [Description("レベル最大値上昇")]
    ReinforcementLevelMaximumUp = 0
    # [Description("レアリティ上昇")]
    RarityUp = 1

# [Description("必要アイテム情報")]
# [MessagePackObject(True)]
@dataclass
class EquipmentEvolutionInfo():
    # [Description("レアリティ")]
    # [PropertyOrder(1)]
    RarityFlags: EquipmentRarityFlags
    # [Description("進化前武具レベル")]
    # [PropertyOrder(2)]
    BeforeEquipmentLv: int
    # [Description("進化後武具レベル")]
    # [PropertyOrder(3)]
    AfterEquipmentLv: int
    # [Description("必要アイテムリスト")]
    # [Nest(True, 1)]
    # [PropertyOrder(4)]
    RequiredItemList: list[UserItem]

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [Description("アイテムのレアリティ")]
# [Flags]
class ItemRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("D")]
    D = 1
    # [Description("C")]
    C = 2
    # [Description("B")]
    B = 4
    # [Description("A")]
    A = 8
    # [Description("S")]
    S = 16
    # [Description("R")]
    R = 32
    # [Description("SR")]
    SR = 64
    # [Description("SSR")]
    SSR = 128
    # [Description("UR")]
    UR = 256
    # [Description("LR")]
    LR = 512

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("属性ボーナス発動段階タイプ")]
class ElementBonusPhaseType(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("段階1")]
    First = 1
    # [Description("段階2")]
    Second = 2
    # [Description("段階3")]
    Third = 3
    # [Description("段階4")]
    Fourth = 4
    # [Description("段階5")]
    Fifth = 5

# [Description("属性条件タイプ")]
class ElementBonusConditionType(Enum):
    # [Description("4属性+天")]
    Default = 0
    # [Description("冥属性")]
    Dark = 1

# [Description("バトルパラメータ変動情報")]
# [MessagePackObject(True)]
@dataclass
class BattleParameterChangeInfo():
    # [Description("変動するバトルパラメータ")]
    # [PropertyOrder(1)]
    BattleParameterType: BattleParameterType
    # [Description("パラメータ増減タイプ")]
    # [PropertyOrder(2)]
    ChangeParameterType: ChangeParameterType
    # [Description("値")]
    # [PropertyOrder(3)]
    Value: float

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("エフェクトグループアイコンタイプ")]
class EffectGroupIconType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("キャラクター")]
    Character = 1
    # [Description("加護")]
    Blessing = 2
    # [Description("敵")]
    Enemy = 3
    # [Description("専属武器")]
    ExclusiveWeapon = 4

# [Description("エフェクトグループアイコンタイプ")]
class EffectGroupIconType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("キャラクター")]
    Character = 1
    # [Description("加護")]
    Blessing = 2
    # [Description("敵")]
    Enemy = 3
    # [Description("専属武器")]
    ExclusiveWeapon = 4

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [MessagePackObject(True)]
@dataclass
class PassiveSkillTypeInfo():
    # [Description("パッシブタイプ")]
    PassiveType: PassiveType
    # [Description("パッシブスキルID")]
    PassiveSkillId: int

# [Description("時空の洞窟 加護レアリティ")]
class DungeonBattleRelicRarityType(Enum):
    None_ = 0
    # [Description("R")]
    R = 1
    # [Description("SR")]
    SR = 2
    # [Description("SSR")]
    SSR = 3

# [Description("時空の洞窟　戦闘力ボーナス対象")]
class DungeonBattleRelicBattlePowerBonusTargetType(Enum):
    # [Description("すべて")]
    All = 0
    # [Description("愁（しゅう）")]
    ElementBlue = 1
    # [Description("業（ごう）")]
    ElementRed = 2
    # [Description("心（しん）")]
    ElementGreen = 3
    # [Description("渇（かつ）")]
    ElementYellow = 4
    # [Description("ウォリアー")]
    Warrior = 5
    # [Description("スナイパー")]
    Sniper = 6
    # [Description("ソーサラー")]
    Sorcerer = 7

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("時空の洞窟 マス種別")]
class DungeonBattleGridType(Enum):
    # [Description("初期地点")]
    Start = 0
    # [Description("バトルマス（通常）")]
    BattleNormal = 1
    # [Description("バトルマス（エリート）")]
    BattleElite = 2
    # [Description("バトルマス（ボス）")]
    BattleBoss = 3
    # [Description("バトルマス（ボス）加護無し")]
    BattleBossNoRelic = 4
    # [Description("回復マス")]
    Recovery = 5
    # [Description("キャラ加入マス")]
    JoinCharacter = 6
    # [Description("ミステリーショップマス")]
    Shop = 7
    # [Description("加護強化マス")]
    RelicReinforce = 8
    # [Description("加護の挑戦マス")]
    BattleAndRelicReinforce = 9
    # [Description("カロンマス")]
    TreasureChest = 10
    # [Description("復活")]
    Revival = 11
    # [Description("イベント通常バトルマス")]
    EventBattleNormal = 12
    # [Description("イベント強敵バトルマス")]
    EventBattleElite = 13
    # [Description("イベント特殊バトルマス")]
    EventBattleSpecial = 14

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [MessagePackObject(True)]
@dataclass
class TransferDetailInfo():
    # [Description("遷移先詳細１")]
    # [PropertyOrder(2)]
    NumberInfo1: int
    # [Description("遷移先詳細２")]
    # [PropertyOrder(3)]
    NumberInfo2: int
    # [Description("遷移先詳細３")]
    # [PropertyOrder(4)]
    StringInfo: str
    # [Description("遷移タイプ")]
    # [PropertyOrder(1)]
    TransferSpotType: TransferSpotType

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("SNS情報")]
# [MessagePackObject(True)]
@dataclass
class SnsInfo():
    # [Description("SNS名称のキー")]
    NameKey: str
    # [Description("URL")]
    Url: str
    # [Description("ミッション達成条件タイプ")]
    MissionAchievementType: MissionAchievementType

# [Description("地域タイプ")]
class CountryCodeType(Enum):
    # [Description("日本")]
    Japan = 0
    # [Description("アメリカ(英語圏)")]
    America = 1
    # [Description("韓国")]
    Korea = 2
    # [Description("台湾")]
    Taiwan = 3

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

# [Description("キャラクターのレアリティ")]
# [Flags]
class CharacterRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("N")]
    N = 1
    # [Description("R")]
    R = 2
    # [Description("R+")]
    RPlus = 4
    # [Description("SR")]
    SR = 8
    # [Description("SR+")]
    SRPlus = 16
    # [Description("SSR")]
    SSR = 32
    # [Description("SSR+")]
    SSRPlus = 64
    # [Description("UR")]
    UR = 128
    # [Description("UR+")]
    URPlus = 256
    # [Description("LR")]
    LR = 512
    # [Description("LR+")]
    LRPlus = 1024
    # [Description("LR+2")]
    LRPlus2 = 2048
    # [Description("LR+3")]
    LRPlus3 = 4096
    # [Description("LR+4")]
    LRPlus4 = 8192
    # [Description("LR+5")]
    LRPlus5 = 16384
    # [Description("LR+6")]
    LRPlus6 = 32768
    # [Description("LR+7")]
    LRPlus7 = 65536

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("ランクアップ·タイプ")]
class ElementClassificationType(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("基本属性")]
    DefaultElement = 1
    # [Description("特殊属性")]
    SpecialElement = 2

# [Description("キャラクターのレアリティ")]
# [Flags]
class CharacterRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("N")]
    N = 1
    # [Description("R")]
    R = 2
    # [Description("R+")]
    RPlus = 4
    # [Description("SR")]
    SR = 8
    # [Description("SR+")]
    SRPlus = 16
    # [Description("SSR")]
    SSR = 32
    # [Description("SSR+")]
    SSRPlus = 64
    # [Description("UR")]
    UR = 128
    # [Description("UR+")]
    URPlus = 256
    # [Description("LR")]
    LR = 512
    # [Description("LR+")]
    LRPlus = 1024
    # [Description("LR+2")]
    LRPlus2 = 2048
    # [Description("LR+3")]
    LRPlus3 = 4096
    # [Description("LR+4")]
    LRPlus4 = 8192
    # [Description("LR+5")]
    LRPlus5 = 16384
    # [Description("LR+6")]
    LRPlus6 = 32768
    # [Description("LR+7")]
    LRPlus7 = 65536

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("ランクアップ·タイプ")]
class RankUpType(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("同一属性")]
    ElementType = 1
    # [Description("同じキャラクターID")]
    SameName = 2

# [Description("キャラクターのレアリティ")]
# [Flags]
class CharacterRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("N")]
    N = 1
    # [Description("R")]
    R = 2
    # [Description("R+")]
    RPlus = 4
    # [Description("SR")]
    SR = 8
    # [Description("SR+")]
    SRPlus = 16
    # [Description("SSR")]
    SSR = 32
    # [Description("SSR+")]
    SSRPlus = 64
    # [Description("UR")]
    UR = 128
    # [Description("UR+")]
    URPlus = 256
    # [Description("LR")]
    LR = 512
    # [Description("LR+")]
    LRPlus = 1024
    # [Description("LR+2")]
    LRPlus2 = 2048
    # [Description("LR+3")]
    LRPlus3 = 4096
    # [Description("LR+4")]
    LRPlus4 = 8192
    # [Description("LR+5")]
    LRPlus5 = 16384
    # [Description("LR+6")]
    LRPlus6 = 32768
    # [Description("LR+7")]
    LRPlus7 = 65536

# [Description("キャラクターのレアリティ")]
# [Flags]
class CharacterRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("N")]
    N = 1
    # [Description("R")]
    R = 2
    # [Description("R+")]
    RPlus = 4
    # [Description("SR")]
    SR = 8
    # [Description("SR+")]
    SRPlus = 16
    # [Description("SSR")]
    SSR = 32
    # [Description("SSR+")]
    SSRPlus = 64
    # [Description("UR")]
    UR = 128
    # [Description("UR+")]
    URPlus = 256
    # [Description("LR")]
    LR = 512
    # [Description("LR+")]
    LRPlus = 1024
    # [Description("LR+2")]
    LRPlus2 = 2048
    # [Description("LR+3")]
    LRPlus3 = 4096
    # [Description("LR+4")]
    LRPlus4 = 8192
    # [Description("LR+5")]
    LRPlus5 = 16384
    # [Description("LR+6")]
    LRPlus6 = 32768
    # [Description("LR+7")]
    LRPlus7 = 65536

# [Description("キャラクターのレアリティ")]
# [Flags]
class CharacterRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("N")]
    N = 1
    # [Description("R")]
    R = 2
    # [Description("R+")]
    RPlus = 4
    # [Description("SR")]
    SR = 8
    # [Description("SR+")]
    SRPlus = 16
    # [Description("SSR")]
    SSR = 32
    # [Description("SSR+")]
    SSRPlus = 64
    # [Description("UR")]
    UR = 128
    # [Description("UR+")]
    URPlus = 256
    # [Description("LR")]
    LR = 512
    # [Description("LR+")]
    LRPlus = 1024
    # [Description("LR+2")]
    LRPlus2 = 2048
    # [Description("LR+3")]
    LRPlus3 = 4096
    # [Description("LR+4")]
    LRPlus4 = 8192
    # [Description("LR+5")]
    LRPlus5 = 16384
    # [Description("LR+6")]
    LRPlus6 = 32768
    # [Description("LR+7")]
    LRPlus7 = 65536

# [Description("キャラクターのレアリティ")]
# [Flags]
class CharacterRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("N")]
    N = 1
    # [Description("R")]
    R = 2
    # [Description("R+")]
    RPlus = 4
    # [Description("SR")]
    SR = 8
    # [Description("SR+")]
    SRPlus = 16
    # [Description("SSR")]
    SSR = 32
    # [Description("SSR+")]
    SSRPlus = 64
    # [Description("UR")]
    UR = 128
    # [Description("UR+")]
    URPlus = 256
    # [Description("LR")]
    LR = 512
    # [Description("LR+")]
    LRPlus = 1024
    # [Description("LR+2")]
    LRPlus2 = 2048
    # [Description("LR+3")]
    LRPlus3 = 4096
    # [Description("LR+4")]
    LRPlus4 = 8192
    # [Description("LR+5")]
    LRPlus5 = 16384
    # [Description("LR+6")]
    LRPlus6 = 32768
    # [Description("LR+7")]
    LRPlus7 = 65536

# [Description("ランクアップ·タイプ")]
class ElementClassificationType(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("基本属性")]
    DefaultElement = 1
    # [Description("特殊属性")]
    SpecialElement = 2

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("各言語に翻訳されたテキスト")]
# [MessagePackObject(True)]
@dataclass
class TranslatedText():
    # [Description("英語")]
    # [PropertyOrder(2)]
    enUS: str
    # [Description("日本語")]
    # [PropertyOrder(1)]
    jaJP: str
    # [Description("韓国語")]
    # [PropertyOrder(3)]
    koKR: str
    # [Description("中国語(繁体字)")]
    # [PropertyOrder(4)]
    zhTW: str

# [Description("各言語に翻訳されたテキスト")]
# [MessagePackObject(True)]
@dataclass
class TranslatedText():
    # [Description("英語")]
    # [PropertyOrder(2)]
    enUS: str
    # [Description("日本語")]
    # [PropertyOrder(1)]
    jaJP: str
    # [Description("韓国語")]
    # [PropertyOrder(3)]
    koKR: str
    # [Description("中国語(繁体字)")]
    # [PropertyOrder(4)]
    zhTW: str

# [Description("キャラクターの血液型")]
class CharacterBloodType(Enum):
    # [Description("不明")]
    None_ = 0
    # [Description("A型")]
    A = 1
    # [Description("B型")]
    B = 2
    # [Description("O型")]
    O = 3
    # [Description("AB型")]
    AB = 4

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("キャラクターのレアリティ")]
# [Flags]
class CharacterRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("N")]
    N = 1
    # [Description("R")]
    R = 2
    # [Description("R+")]
    RPlus = 4
    # [Description("SR")]
    SR = 8
    # [Description("SR+")]
    SRPlus = 16
    # [Description("SSR")]
    SSR = 32
    # [Description("SSR+")]
    SSRPlus = 64
    # [Description("UR")]
    UR = 128
    # [Description("UR+")]
    URPlus = 256
    # [Description("LR")]
    LR = 512
    # [Description("LR+")]
    LRPlus = 1024
    # [Description("LR+2")]
    LRPlus2 = 2048
    # [Description("LR+3")]
    LRPlus3 = 4096
    # [Description("LR+4")]
    LRPlus4 = 8192
    # [Description("LR+5")]
    LRPlus5 = 16384
    # [Description("LR+6")]
    LRPlus6 = 32768
    # [Description("LR+7")]
    LRPlus7 = 65536

# [MessagePackObject(True)]
@dataclass
class CharacterRarityCoefficientInfo():
    m: float
    b: int

# [Description("キャラクターのレアリティ")]
# [Flags]
class CharacterRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("N")]
    N = 1
    # [Description("R")]
    R = 2
    # [Description("R+")]
    RPlus = 4
    # [Description("SR")]
    SR = 8
    # [Description("SR+")]
    SRPlus = 16
    # [Description("SSR")]
    SSR = 32
    # [Description("SSR+")]
    SSRPlus = 64
    # [Description("UR")]
    UR = 128
    # [Description("UR+")]
    URPlus = 256
    # [Description("LR")]
    LR = 512
    # [Description("LR+")]
    LRPlus = 1024
    # [Description("LR+2")]
    LRPlus2 = 2048
    # [Description("LR+3")]
    LRPlus3 = 4096
    # [Description("LR+4")]
    LRPlus4 = 8192
    # [Description("LR+5")]
    LRPlus5 = 16384
    # [Description("LR+6")]
    LRPlus6 = 32768
    # [Description("LR+7")]
    LRPlus7 = 65536

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("キャラクターのレアリティ")]
# [Flags]
class CharacterRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("N")]
    N = 1
    # [Description("R")]
    R = 2
    # [Description("R+")]
    RPlus = 4
    # [Description("SR")]
    SR = 8
    # [Description("SR+")]
    SRPlus = 16
    # [Description("SSR")]
    SSR = 32
    # [Description("SSR+")]
    SSRPlus = 64
    # [Description("UR")]
    UR = 128
    # [Description("UR+")]
    URPlus = 256
    # [Description("LR")]
    LR = 512
    # [Description("LR+")]
    LRPlus = 1024
    # [Description("LR+2")]
    LRPlus2 = 2048
    # [Description("LR+3")]
    LRPlus3 = 4096
    # [Description("LR+4")]
    LRPlus4 = 8192
    # [Description("LR+5")]
    LRPlus5 = 16384
    # [Description("LR+6")]
    LRPlus6 = 32768
    # [Description("LR+7")]
    LRPlus7 = 65536

# [Description("職業")]
# [Flags]
class JobFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("ウォリアー")]
    Warrior = 1
    # [Description("スナイパー")]
    Sniper = 2
    # [Description("ソーサラー")]
    Sorcerer = 4

# [Description("アイテムのレアリティ")]
# [Flags]
class ItemRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("D")]
    D = 1
    # [Description("C")]
    C = 2
    # [Description("B")]
    B = 4
    # [Description("A")]
    A = 8
    # [Description("S")]
    S = 16
    # [Description("R")]
    R = 32
    # [Description("SR")]
    SR = 64
    # [Description("SSR")]
    SSR = 128
    # [Description("UR")]
    UR = 256
    # [Description("LR")]
    LR = 512

# [Description("バトルパラメータ")]
# [MessagePackObject(True)]
@dataclass
class BattleParameter():
    # [Description("攻撃力")]
    AttackPower: int
    # [Description("回避")]
    Avoidance: int
    # [Description("クリティカル")]
    Critical: int
    # [Description("クリダメ強化")]
    CriticalDamageEnhance: int
    # [Description("クリティカル耐性")]
    CriticalResist: int
    # [Description("ダメージ強化")]
    DamageEnhance: int
    # [Description("カウンタ​")]
    DamageReflect: int
    # [Description("弱体効果命中​")]
    DebuffHit: int
    # [Description("弱体効果耐性")]
    DebuffResist: int
    # [Description("防御力")]
    Defense: int
    # [Description("防御貫通力")]
    DefensePenetration: int
    # [Description("命中")]
    Hit: int
    # [Description("HP")]
    HP: int
    # [Description("HP吸収")]
    HpDrain: int
    # [Description("魔法クリダメ緩和")]
    MagicCriticalDamageRelax: int
    # [Description("魔法ダメージ緩和")]
    MagicDamageRelax: int
    # [Description("物理クリダメ緩和")]
    PhysicalCriticalDamageRelax: int
    # [Description("物理ダメージ緩和")]
    PhysicalDamageRelax: int
    # [Description("スピード​")]
    Speed: int

class ElementType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("愁（しゅう）")]
    Blue = 1
    # [Description("業（ごう）")]
    Red = 2
    # [Description("心（しん）")]
    Green = 3
    # [Description("渇（かつ）")]
    Yellow = 4
    # [Description("天（てん） ")]
    Light = 5
    # [Description("冥（めい） ")]
    Dark = 6

class CharacterType(Enum):
    Normal = 0
    Qlipha = 1
    ColorChange = 2

# [Description("基礎パラメータ")]
# [MessagePackObject(True)]
@dataclass
class BaseParameter():
    # [Description("技力​")]
    Energy: int
    # [Description("耐久力​")]
    Health: int
    # [Description("魔力")]
    Intelligence: int
    # [Description("筋力")]
    Muscle: int

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("視聴可能ボイスの解放条件")]
class UnlockCharacterDetailVoiceType(Enum):
    # [Description("条件無し")]
    None_ = 0
    # [Description("ランクアップボイス1")]
    RankUp1 = 1
    # [Description("ランクアップボイス2")]
    RankUp2 = 2
    # [Description("ランクアップボイス3")]
    RankUp3 = 3
    # [Description("ランクアップボイス4")]
    RankUp4 = 4
    # [Description("ランクアップボイス5")]
    RankUp5 = 5
    # [Description("ランクアップボイス6")]
    RankUp6 = 6
    # [Description("誕生日")]
    Birthday = 7
    # [Description("メモリー全視聴")]
    MemoryComplete = 8
    # [Description("クエストクリア")]
    QuestClear = 9

# [MessagePackObject(True)]
@dataclass
class CharacterVoicePath():
    # [Description("TimelineId")]
    # [PropertyOrder(2)]
    TimelineId: int
    # [Description("TimelineType")]
    # [PropertyOrder(1)]
    TimelineType: TimelineType

# [Description("キャラクターボイスの分類")]
class CharacterVoiceCategory(Enum):
    # [Description("通常セリフ")]
    Basic = 0
    # [Description("誕生日セリフ")]
    Birthday = 1
    # [Description("カムバックセリフ")]
    ComeBack = 2
    # [Description("ログインセリフ")]
    Login = 3
    # [Description("ランクアップセリフ")]
    RankUp = 4
    # [Description("その他")]
    Other = 5
    # [Description("登場")]
    Appear = 6
    # [Description("決め台詞")]
    SignaturePhrase = 7
    # [Description("バトル勝利")]
    BattleWin = 8
    # [Description("バトル敗北")]
    BattleLose = 9

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("キャラクターのレアリティ")]
# [Flags]
class CharacterRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("N")]
    N = 1
    # [Description("R")]
    R = 2
    # [Description("R+")]
    RPlus = 4
    # [Description("SR")]
    SR = 8
    # [Description("SR+")]
    SRPlus = 16
    # [Description("SSR")]
    SSR = 32
    # [Description("SSR+")]
    SSRPlus = 64
    # [Description("UR")]
    UR = 128
    # [Description("UR+")]
    URPlus = 256
    # [Description("LR")]
    LR = 512
    # [Description("LR+")]
    LRPlus = 1024
    # [Description("LR+2")]
    LRPlus2 = 2048
    # [Description("LR+3")]
    LRPlus3 = 4096
    # [Description("LR+4")]
    LRPlus4 = 8192
    # [Description("LR+5")]
    LRPlus5 = 16384
    # [Description("LR+6")]
    LRPlus6 = 32768
    # [Description("LR+7")]
    LRPlus7 = 65536

# [Description("バトルパラメータ変動情報")]
# [MessagePackObject(True)]
@dataclass
class BattleParameterChangeInfo():
    # [Description("変動するバトルパラメータ")]
    # [PropertyOrder(1)]
    BattleParameterType: BattleParameterType
    # [Description("パラメータ増減タイプ")]
    # [PropertyOrder(2)]
    ChangeParameterType: ChangeParameterType
    # [Description("値")]
    # [PropertyOrder(3)]
    Value: float

# [Description("基礎パラメータ変動情報")]
# [MessagePackObject(True)]
@dataclass
class BaseParameterChangeInfo():
    # [Description("変動する基礎パラメータ")]
    # [PropertyOrder(1)]
    BaseParameterType: BaseParameterType
    # [Description("パラメータ増減タイプ")]
    # [PropertyOrder(2)]
    ChangeParameterType: ChangeParameterType
    # [Description("値")]
    # [PropertyOrder(3)]
    Value: float

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("アイテムの種類")]
class ItemType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("無償仮想通貨")]
    CurrencyFree = 1
    # [Description("有償仮想通貨")]
    CurrencyPaid = 2
    # [Description("ゲーム内通貨")]
    Gold = 3
    # [Description("武具")]
    Equipment = 4
    # [Description("武具の欠片")]
    EquipmentFragment = 5
    # [Description("キャラクター")]
    Character = 6
    # [Description("キャラクターの絆")]
    CharacterFragment = 7
    # [Description("洞窟の加護")]
    DungeonBattleRelic = 8
    # [Description("アダマンタイト")]
    EquipmentSetMaterial = 9
    # [Description("n時間分アイテム")]
    QuestQuickTicket = 10
    # [Description("キャラ育成素材")]
    CharacterTrainingMaterial = 11
    # [Description("武具強化アイテム")]
    EquipmentReinforcementItem = 12
    # [Description("交換所アイテム")]
    ExchangePlaceItem = 13
    # [Description("スフィア")]
    Sphere = 14
    # [Description("魔装強化アイテム")]
    MatchlessSacredTreasureExpItem = 15
    # [Description("ガチャチケット")]
    GachaTicket = 16
    # [Description("宝箱、未鑑定スフィアなど")]
    TreasureChest = 17
    # [Description("宝箱の鍵")]
    TreasureChestKey = 18
    # [Description("ボスチケット")]
    BossChallengeTicket = 19
    # [Description("無窮の塔チケット")]
    TowerBattleTicket = 20
    # [Description("回復の果実")]
    DungeonRecoveryItem = 21
    # [Description("プレイヤー経験値")]
    PlayerExp = 22
    # [Description("フレンドポイント")]
    FriendPoint = 23
    # [Description("生命樹の雫")]
    EquipmentRarityCrystal = 24
    # [Description("レベルリンク経験値")]
    LevelLinkExp = 25
    # [Description("ギルドストック")]
    GuildFame = 26
    # [Description("ギルド経験値")]
    GuildExp = 27
    # [Description("貢献メダル")]
    ActivityMedal = 28
    # [Description("イベント交換所アイテム")]
    EventExchangePlaceItem = 50

# [Description("アイテム変換タイプ")]
class ChangeItemType(Enum):
    # [Description("販売")]
    Sell = 0
    # [Description("合成")]
    Compose = 1

# [MessagePackObject(True)]
@dataclass
class UserItem():
    ItemCount: int
    ItemId: int
    ItemType: ItemType

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [MessagePackObject(True)]
@dataclass
class BountyQuestEventTargetQuestTypeInfo():
    BountyQuestType: BountyQuestType

# [MessagePackObject(True)]
@dataclass
class BountyQuestEventTargetItemInfo():
    ItemId: int
    ItemType: ItemType

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

class UnitIconType(Enum):
    # [Description("キャラクター")]
    Character = 0
    # [Description("敵キャラクター")]
    EnemyCharacter = 1
    # [Description("魔女クリファ")]
    WitchQlipha = 2

# [Description("職業")]
# [Flags]
class JobFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("ウォリアー")]
    Warrior = 1
    # [Description("スナイパー")]
    Sniper = 2
    # [Description("ソーサラー")]
    Sorcerer = 4

class ElementType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("愁（しゅう）")]
    Blue = 1
    # [Description("業（ごう）")]
    Red = 2
    # [Description("心（しん）")]
    Green = 3
    # [Description("渇（かつ）")]
    Yellow = 4
    # [Description("天（てん） ")]
    Light = 5
    # [Description("冥（めい） ")]
    Dark = 6

# [Description("キャラクターのレアリティ")]
# [Flags]
class CharacterRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("N")]
    N = 1
    # [Description("R")]
    R = 2
    # [Description("R+")]
    RPlus = 4
    # [Description("SR")]
    SR = 8
    # [Description("SR+")]
    SRPlus = 16
    # [Description("SSR")]
    SSR = 32
    # [Description("SSR+")]
    SSRPlus = 64
    # [Description("UR")]
    UR = 128
    # [Description("UR+")]
    URPlus = 256
    # [Description("LR")]
    LR = 512
    # [Description("LR+")]
    LRPlus = 1024
    # [Description("LR+2")]
    LRPlus2 = 2048
    # [Description("LR+3")]
    LRPlus3 = 4096
    # [Description("LR+4")]
    LRPlus4 = 8192
    # [Description("LR+5")]
    LRPlus5 = 16384
    # [Description("LR+6")]
    LRPlus6 = 32768
    # [Description("LR+7")]
    LRPlus7 = 65536

# [Description("バトルパラメータ")]
# [MessagePackObject(True)]
@dataclass
class BattleParameter():
    # [Description("攻撃力")]
    AttackPower: int
    # [Description("回避")]
    Avoidance: int
    # [Description("クリティカル")]
    Critical: int
    # [Description("クリダメ強化")]
    CriticalDamageEnhance: int
    # [Description("クリティカル耐性")]
    CriticalResist: int
    # [Description("ダメージ強化")]
    DamageEnhance: int
    # [Description("カウンタ​")]
    DamageReflect: int
    # [Description("弱体効果命中​")]
    DebuffHit: int
    # [Description("弱体効果耐性")]
    DebuffResist: int
    # [Description("防御力")]
    Defense: int
    # [Description("防御貫通力")]
    DefensePenetration: int
    # [Description("命中")]
    Hit: int
    # [Description("HP")]
    HP: int
    # [Description("HP吸収")]
    HpDrain: int
    # [Description("魔法クリダメ緩和")]
    MagicCriticalDamageRelax: int
    # [Description("魔法ダメージ緩和")]
    MagicDamageRelax: int
    # [Description("物理クリダメ緩和")]
    PhysicalCriticalDamageRelax: int
    # [Description("物理ダメージ緩和")]
    PhysicalDamageRelax: int
    # [Description("スピード​")]
    Speed: int

# [Description("基礎パラメータ")]
# [MessagePackObject(True)]
@dataclass
class BaseParameter():
    # [Description("技力​")]
    Energy: int
    # [Description("耐久力​")]
    Health: int
    # [Description("魔力")]
    Intelligence: int
    # [Description("筋力")]
    Muscle: int

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("祈りの泉クエストレアリティ")]
# [Flags]
class BountyQuestRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("N*")]
    NInit = 1
    # [Description("N")]
    N = 2
    # [Description("R")]
    R = 4
    # [Description("SR")]
    SR = 8
    # [Description("SSR")]
    SSR = 16
    # [Description("UR")]
    UR = 32
    # [Description("LR")]
    LR = 64

# [Description("祈りの泉クエストレアリティ")]
# [Flags]
class BountyQuestRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("N*")]
    NInit = 1
    # [Description("N")]
    N = 2
    # [Description("R")]
    R = 4
    # [Description("SR")]
    SR = 8
    # [Description("SSR")]
    SSR = 16
    # [Description("UR")]
    UR = 32
    # [Description("LR")]
    LR = 64

# [MessagePackObject(True)]
@dataclass
class BoardRankConditionInfo():
    # [Description("懸賞カウンタークエストタイプ")]
    BountyQuestType: BountyQuestType
    # [Description("クエストレベル")]
    BountyQuestRarity: BountyQuestRarityFlags
    # [Description("必要な数")]
    RequireCount: int
    # [Description("累計必要クリア数")]
    TotalRequireCount: int

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

class CharacterColorType(Enum):
    None_ = 0
    BluePurple = 1
    BlueGreen = 2
    RedPeach = 3
    BrightYellow = 4
    Gray = 5

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("バトルタイプ")]
class BattleScheduleType(Enum):
    # [Description("バトルタイプなし")]
    None_ = 0
    # [Description("クエスト(ボス、オートバトル)")]
    Quest = 1
    # [Description("無窮の塔")]
    TowerInfinite = 2
    # [Description("愁（しゅう）")]
    TowerBlue = 3
    # [Description("業（ごう）")]
    TowerRed = 4
    # [Description("心（しん）")]
    TowerGreen = 5
    # [Description("渇（かつ）")]
    TowerYellow = 6

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

class UnitIconType(Enum):
    # [Description("キャラクター")]
    Character = 0
    # [Description("敵キャラクター")]
    EnemyCharacter = 1
    # [Description("魔女クリファ")]
    WitchQlipha = 2

# [Description("職業")]
# [Flags]
class JobFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("ウォリアー")]
    Warrior = 1
    # [Description("スナイパー")]
    Sniper = 2
    # [Description("ソーサラー")]
    Sorcerer = 4

class ElementType(Enum):
    # [Description("なし")]
    None_ = 0
    # [Description("愁（しゅう）")]
    Blue = 1
    # [Description("業（ごう）")]
    Red = 2
    # [Description("心（しん）")]
    Green = 3
    # [Description("渇（かつ）")]
    Yellow = 4
    # [Description("天（てん） ")]
    Light = 5
    # [Description("冥（めい） ")]
    Dark = 6

# [Description("キャラクターのレアリティ")]
# [Flags]
class CharacterRarityFlags(Enum):
    # [Description("None")]
    None_ = 0
    # [Description("N")]
    N = 1
    # [Description("R")]
    R = 2
    # [Description("R+")]
    RPlus = 4
    # [Description("SR")]
    SR = 8
    # [Description("SR+")]
    SRPlus = 16
    # [Description("SSR")]
    SSR = 32
    # [Description("SSR+")]
    SSRPlus = 64
    # [Description("UR")]
    UR = 128
    # [Description("UR+")]
    URPlus = 256
    # [Description("LR")]
    LR = 512
    # [Description("LR+")]
    LRPlus = 1024
    # [Description("LR+2")]
    LRPlus2 = 2048
    # [Description("LR+3")]
    LRPlus3 = 4096
    # [Description("LR+4")]
    LRPlus4 = 8192
    # [Description("LR+5")]
    LRPlus5 = 16384
    # [Description("LR+6")]
    LRPlus6 = 32768
    # [Description("LR+7")]
    LRPlus7 = 65536

# [Description("バトルパラメータ")]
# [MessagePackObject(True)]
@dataclass
class BattleParameter():
    # [Description("攻撃力")]
    AttackPower: int
    # [Description("回避")]
    Avoidance: int
    # [Description("クリティカル")]
    Critical: int
    # [Description("クリダメ強化")]
    CriticalDamageEnhance: int
    # [Description("クリティカル耐性")]
    CriticalResist: int
    # [Description("ダメージ強化")]
    DamageEnhance: int
    # [Description("カウンタ​")]
    DamageReflect: int
    # [Description("弱体効果命中​")]
    DebuffHit: int
    # [Description("弱体効果耐性")]
    DebuffResist: int
    # [Description("防御力")]
    Defense: int
    # [Description("防御貫通力")]
    DefensePenetration: int
    # [Description("命中")]
    Hit: int
    # [Description("HP")]
    HP: int
    # [Description("HP吸収")]
    HpDrain: int
    # [Description("魔法クリダメ緩和")]
    MagicCriticalDamageRelax: int
    # [Description("魔法ダメージ緩和")]
    MagicDamageRelax: int
    # [Description("物理クリダメ緩和")]
    PhysicalCriticalDamageRelax: int
    # [Description("物理ダメージ緩和")]
    PhysicalDamageRelax: int
    # [Description("スピード​")]
    Speed: int

# [Description("基礎パラメータ")]
# [MessagePackObject(True)]
@dataclass
class BaseParameter():
    # [Description("技力​")]
    Energy: int
    # [Description("耐久力​")]
    Health: int
    # [Description("魔力")]
    Intelligence: int
    # [Description("筋力")]
    Muscle: int

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("端末&プラットフォーム種別")]
class DeviceType(Enum):
    # [Description("iOS")]
    iOS = 1
    # [Description("Android")]
    Android = 2
    # [Description("Unity")]
    UnityEditor = 3
    # [Description("Windows")]
    Win64 = 4
    # [Description("DmmGames")]
    DmmGames = 5
    # [Description("Steam")]
    Steam = 6
    # [Description("BlueStacks")]
    BlueStacks = 7

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [MessagePackObject(True)]
@dataclass
class ActiveSkillInfo():
    # [Description("優先順位")]
    OrderNumber: int
    # [Description("スキル説明文キー")]
    DescriptionKey: str
    # [Description("キャラクターレベル制限")]
    CharacterLevel: int
    # [Description("専属武具レアリティ")]
    EquipmentRarityFlags: EquipmentRarityFlags
    # [Description("加護ID")]
    BlessingItemId: int
    # [Description("サブセットIDリスト")]
    SubSetSkillIds: list[int]

@dataclass
class MasterBookBase():
    Id: int
    IsIgnore: bool | None
    Memo: str

# [Description("ワールドグループ")]
# [MessagePackObject(True)]
@dataclass
class WorldGroupMB(MasterBookBase):
    # [Description("終了日時")]
    # [PropertyOrder(5)]
    EndTime: str
    # [Description("グランドバトル終了日時")]
    # [PropertyOrder(7)]
    EndGrandBattleDateTime: str
    # [Description("レジェンドリーグ終了日時")]
    # [PropertyOrder(9)]
    EndLegendLeagueDateTime: str
    # [Description("タイムサーバー")]
    # [PropertyOrder(1)]
    TimeServerId: int
    # [Description("開始日時")]
    # [PropertyOrder(4)]
    StartTime: str
    # [Description("グランドバトル開始日時")]
    # [PropertyOrder(6)]
    StartGrandBattleDateTime: str
    # [Description("レジェンドリーグ開始日時")]
    # [PropertyOrder(8)]
    StartLegendLeagueDateTime: str
    # [Description("WorldIdのリスト")]
    # [PropertyOrder(3)]
    WorldIdList: list[int]

# [Description("VIP特典")]
# [MessagePackObject(True)]
@dataclass
class VipMB(MasterBookBase):
    # [Description("放置バトル経験値ボーナス(%)")]
    # [PropertyOrder(3)]
    AutoBattlePlayerExpBonus: int
    # [Description("VIPデイリー報酬リスト")]
    # [Nest(False, 0)]
    # [PropertyOrder(25)]
    DailyRewardItemList: list[UserItem]
    # [Description("時空の洞窟コインドロップ増加​(%)")]
    # [PropertyOrder(9)]
    DungeonBattleCoinBonus: int
    # [Description("時空の洞窟ゴールドボーナス(%)")]
    # [PropertyOrder(10)]
    DungeonBattleGoldBonus: int
    # [Description("時空の洞窟：見逃し可能回数")]
    # [PropertyOrder(13)]
    DungeonBattleMissedCompensationCount: int
    # [Description("運命ガチャが可能か否か")]
    # [PropertyOrder(18)]
    IsDestinyGachaAvailable: bool
    # [Description("運命ガチャのログが見れるか否か")]
    # [PropertyOrder(19)]
    IsDestinyGachaLogAvailable: bool
    # [Description("研磨時にロックが可能か否か​")]
    # [PropertyOrder(22)]
    IsLockEquipmentTrainingAvailable: bool
    # [Description("祈りの泉一括派遣、受け取り​が可能か否か")]
    # [PropertyOrder(15)]
    IsMultipleBountyQuestAvailable: bool
    # [Description("ボス/無窮の塔掃討が可能か否か")]
    # [PropertyOrder(20)]
    IsQuickBossBattleAvailable: bool
    # [Description("ギルドレイドの掃討が可能か否か")]
    # [PropertyOrder(17)]
    IsQuickStartGuildRaidAvailable: bool
    # [Description("神装強化の装備返還が可能か否か​")]
    # [PropertyOrder(21)]
    IsRefundEquipmentMergeAvailable: bool
    # [Description("ログインボーナス見逃し補填回数")]
    # [PropertyOrder(14)]
    LoginBonusMissedCompensationCount: int
    # [Description("VIPレベル")]
    # [PropertyOrder(1)]
    Lv: int
    # [Description("ボス/無窮の塔挑戦購入可能回数増加​")]
    # [PropertyOrder(11)]
    MaxBossBattleUseCurrencyCount: int
    # [Description("英雄枠数増加​")]
    # [PropertyOrder(8)]
    MaxCharacterBoxPlus: int
    # [Description("ギルドレイド挑戦可能回数")]
    # [PropertyOrder(16)]
    MaxGuildRaidChallengeCount: int
    # [Description("仮想通貨で高速周回できる回数")]
    # [PropertyOrder(5)]
    MaxQuickUseCurrencyCount: int
    # [Description("ショップの アイテム数増加​")]
    # [PropertyOrder(12)]
    MaxShopItemCountPlus: int
    # [Description("ソロクエストを挑戦できる回数")]
    # [PropertyOrder(6)]
    MaxSoloQuestCount: int
    # [Description("チームクエストを挑戦できる回数")]
    # [PropertyOrder(7)]
    MaxTeamQuestCount: int
    # [Description("高速戦闘経験値ボーナス(%)")]
    # [PropertyOrder(5)]
    QuickBattlePlayerExpBonus: int
    # [Description("VIP到達時報酬リスト")]
    # [Nest(False, 0)]
    # [PropertyOrder(23)]
    ReachRewardItemList: list[UserItem]
    # [Description("必要累計 VIP経験値")]
    # [PropertyOrder(2)]
    RequiredExp: int
    # [Description("VIPギフトリスト")]
    # [Nest(True, 0)]
    # [PropertyOrder(24)]
    VipGiftInfoList: list[VipGiftInfo]

# [Description("チュートリアルテキストボックス")]
# [MessagePackObject(True)]
@dataclass
class TutorialTextBoxMB(MasterBookBase):
    # [Description("キャラアイコンのキャラID")]
    # [PropertyOrder(2)]
    CharacterId: int
    # [Description("テキストキー")]
    # [PropertyOrder(1)]
    TextKey: str
    # [Description("ボイスファイルパス")]
    # [PropertyOrder(3)]
    VoiceJPFilePath: str
    # [Description("ボイスファイルパス")]
    # [PropertyOrder(4)]
    VoiceUSFilePath: str

# [Description("チュートリアル詳細")]
# [MessagePackObject(True)]
@dataclass
class TutorialDescriptionMB(MasterBookBase):
    # [Description("HelpMB ID(チュートリアル用)")]
    # [PropertyOrder(2)]
    HelpId: int
    # [Description("可変画像アイテム1")]
    # [Nest(False, 0)]
    # [PropertyOrder(4)]
    ImageItem1: UserItem
    # [Description("可変画像アイテム2")]
    # [Nest(False, 0)]
    # [PropertyOrder(5)]
    ImageItem2: UserItem
    # [Description("画像位置フォーマットタイプ")]
    # [PropertyOrder(3)]
    ImagePositionFormatType: ImagePositionFormatType
    # [Description("ページ情報")]
    # [Nest(False, 0)]
    # [PropertyOrder(1)]
    PageInfo: list[TutorialDescriptionPageInfo]
    # [Description("可変画像キャラID")]
    # [PropertyOrder(6)]
    ImageCharacterId: int

# [Description("宝箱、宝石袋など")]
# [MessagePackObject(True)]
@dataclass
class TreasureChestMB(MasterBookBase):
    # [Description("開けるのに必要な鍵のID ※0の場合無効")]
    # [PropertyOrder(7)]
    ChestKeyItemId: int
    # [Description("説明文キー")]
    # [PropertyOrder(3)]
    DescriptionKey: str
    # [Description("表示名キー")]
    # [PropertyOrder(2)]
    DisplayNameKey: str
    # [Description("アイコンID")]
    # [PropertyOrder(4)]
    IconId: int
    # [Description("レアリティ")]
    # [PropertyOrder(5)]
    ItemRarityFlags: ItemRarityFlags
    # [Description("所持数上限")]
    # [PropertyOrder(9)]
    MaxItemCount: int
    # [Description("必要個数")]
    # [PropertyOrder(8)]
    MinOpenCount: int
    # [Description("名称キー")]
    # [PropertyOrder(1)]
    NameKey: str
    # [Description("第2フレーム値")]
    # [PropertyOrder(11)]
    SecondaryFrameNum: int
    # [Description("第2フラーム種類")]
    # [PropertyOrder(10)]
    SecondaryFrameType: SecondaryFrameType
    # [Description("TreasureChestItemMBのIdリスト")]
    # [PropertyOrder(12)]
    TreasureChestItemIdList: list[int]
    # [Description("宝箱の報酬判定方法タイプ")]
    # [PropertyOrder(6)]
    TreasureChestLotteryType: TreasureChestLotteryType
    # [Description("終了日時")]
    # [PropertyOrder(13)]
    EndTime: str
    # [Description("開始日時")]
    # [PropertyOrder(14)]
    StartTime: str

# [Description("宝箱から得られるアイテム")]
# [MessagePackObject(True)]
@dataclass
class TreasureChestItemMB(MasterBookBase):
    # [Description("固定アイテムリスト")]
    # [Nest(True, 1)]
    # [PropertyOrder(4)]
    FixItemList: list[TreasureChestFixItem]
    # [Description("抽選報酬ID")]
    # [PropertyOrder(2)]
    LotteryRewardId: int
    # [Description("選択アイテムリスト")]
    # [Nest(True, 0)]
    # [PropertyOrder(3)]
    SelectItemList: list[TreasureChestSelectItem]
    # [Description("ItemListの参照先")]
    # [PropertyOrder(1)]
    TreasureChestItemListType: TreasureChestItemListType

# [Description("宝箱天井設定")]
# [MessagePackObject(True)]
@dataclass
class TreasureChestCeilingMB(MasterBookBase):
    # [Description("天井条件回数")]
    # [PropertyOrder(2)]
    CeilingCount: int
    # [Description("天井を適用するTreasureChestItemのId")]
    # [PropertyOrder(1)]
    TreasureChestItemId: int

# [Description("交換所タブ")]
# [MessagePackObject(True)]
@dataclass
class TradeShopTabMB(MasterBookBase):
    # [Description("定期自動更新(タイプ４の更新時間)")]
    # [PropertyOrder(14)]
    AutoUpdateTimes: list[int]
    # [Description("定期自動更新タイプ")]
    # [PropertyOrder(13)]
    AutoUpdateType: TradeShopAutoUpdateType
    # [Description("消費アイテムリスト(表示用)")]
    # [Nest(False, 0)]
    # [PropertyOrder(17)]
    ConsumeItemInfos: list[ConsumeItemInfo]
    # [Description("レイアウト")]
    # [Nest(False, 0)]
    # [PropertyOrder(6)]
    CustomTextLayout: CustomTextLayout
    # [Description("デコレーション色")]
    # [PropertyOrder(5)]
    DecorationColor: str
    # [Description("デコレーションId")]
    # [PropertyOrder(3)]
    DecorationId: int
    # [Description("デコレーションスペシャルId")]
    # [PropertyOrder(4)]
    DecorationSpecialId: int
    # [Description("アイコンId")]
    # [PropertyOrder(2)]
    IconId: int
    # [Description("強制非表示フラグ")]
    # [PropertyOrder(9)]
    IsHide: bool
    # [Description("未解放時に非表示にするフラグ")]
    # [PropertyOrder(11)]
    IsHideNotOpen: bool
    # [Description("手動更新可能フラグ")]
    # [PropertyOrder(15)]
    IsManualUpdate: bool
    # [Description("手動更新に必要なダイヤ数")]
    # [PropertyOrder(16)]
    ManualUpdateCurrencyCount: int
    # [Description("コンテンツ実行タイプ")]
    # [PropertyOrder(18)]
    OpenCommandType: OpenCommandType
    # [Description("並び順")]
    # [PropertyOrder(8)]
    SortOrder: int
    # [Description("タブ名")]
    # [PropertyOrder(7)]
    TabNameKey: str
    # [Description("店舗景品数")]
    # [PropertyOrder(17)]
    TradeShopItemCount: int
    # [Description("交換所種類")]
    # [PropertyOrder(12)]
    TradeShopType: TradeShopType
    # [Description("終了日時")]
    # [PropertyOrder(20)]
    EndTime: str
    # [Description("開始日時")]
    # [PropertyOrder(19)]
    StartTime: str

# [Description("交換所スフィア")]
# [MessagePackObject(True)]
@dataclass
class TradeShopSphereMB(MasterBookBase):
    # [Description("スフィアのLv")]
    # [PropertyOrder(1)]
    SphereLevel: int
    # [Description("消費アイテム1")]
    # [Nest(False, 0)]
    # [PropertyOrder(2)]
    ConsumeItem1: UserItem
    # [Description("消費アイテム2")]
    # [Nest(False, 0)]
    # [PropertyOrder(3)]
    ConsumeItem2: UserItem

# [Description("無窮の塔　階層情報")]
# [MessagePackObject(True)]
@dataclass
class TowerBattleQuestMB(MasterBookBase):
    # [Description("クリアパーティの基準（ベース）戦闘力")]
    # [PropertyOrder(3)]
    BaseClearPartyDeckPower: int
    # [Description("確定獲得クリア報酬")]
    # [Nest(False, 0)]
    # [PropertyOrder(6)]
    BattleRewardsConfirmed: list[UserItem]
    # [Description("初回獲得クリア報酬")]
    # [Nest(False, 0)]
    # [PropertyOrder(5)]
    BattleRewardsFirst: list[UserItem]
    # [Description("敵IDリスト")]
    # [PropertyOrder(4)]
    EnemyIds: list[int]
    # [Description("階層")]
    # [PropertyOrder(2)]
    Floor: int
    # [Description("抽選報酬情報")]
    # [PropertyOrder(7)]
    LotteryRewardInfoId: int
    # [Description("塔の種類")]
    # [PropertyOrder(1)]
    TowerType: TowerType

# [Description("無窮の塔　敵データ")]
# [MessagePackObject(True)]
@dataclass
class TowerBattleEnemyMB(MasterBookBase):
    # [Description("アクティブスキルIDのリスト")]
    # [PropertyOrder(15)]
    ActiveSkillIds: list[int]
    # [Description("ベースパラメータ")]
    # [Nest(True, 1)]
    # [PropertyOrder(5)]
    BaseParameter: BaseParameter
    # [Description("敵キャラクターID")]
    # [PropertyOrder(1)]
    BattleEnemyCharacterId: int
    # [Description("バトルパラメータ")]
    # [Nest(True, 1)]
    # [PropertyOrder(6)]
    BattleParameter: BattleParameter
    # [Description("戦闘力")]
    # [PropertyOrder(7)]
    BattlePower: int
    # [Description("レアリティ")]
    # [PropertyOrder(4)]
    CharacterRarityFlags: CharacterRarityFlags
    # [Description("属性")]
    # [PropertyOrder(11)]
    ElementType: ElementType
    # [Description("敵調整値ID")]
    # [PropertyOrder(8)]
    EnemyAdjustId: int
    # [Description("敵武具ID")]
    # [PropertyOrder(2)]
    EnemyEquipmentId: int
    # [Description("敵のランク")]
    # [PropertyOrder(3)]
    EnemyRank: int
    # [Description("職業")]
    # [PropertyOrder(10)]
    JobFlags: JobFlags
    # [Description("名称キー")]
    # [PropertyOrder(9)]
    NameKey: str
    # [Description("通常攻撃として使ってくるスキルID")]
    # [PropertyOrder(14)]
    NormalSkillId: int
    # [Description("パッシブスキルIDのリスト")]
    # [PropertyOrder(16)]
    PassiveSkillIds: list[int]
    # [Description("ユニットアイコンID")]
    # [PropertyOrder(13)]
    UnitIconId: int
    # [Description("ユニットアイコンタイプ")]
    # [PropertyOrder(12)]
    UnitIconType: UnitIconType

# [Description("累計貢献メダル報酬")]
# [MessagePackObject(True)]
@dataclass
class TotalActivityMedalRewardMB(MasterBookBase):
    # [Description("ミッション種別")]
    # [PropertyOrder(1)]
    MissionGroupType: MissionGroupType
    # [Description("必要貢献メダル")]
    # [PropertyOrder(2)]
    RequiredActivityMedalCount: int
    # [Description("報酬リスト")]
    # [Nest(False, 0)]
    # [PropertyOrder(3)]
    RewardList: list[MissionReward]
    # [Description("イベント開始時刻")]
    # [PropertyOrder(4)]
    EventStartTime: str
    # [Description("イベント終了時刻")]
    # [PropertyOrder(5)]
    EventEndTime: str
    # [Description("イベント報酬リスト")]
    # [Nest(False, 0)]
    # [PropertyOrder(6)]
    EventMissionRewardList: list[EventMissionReward]

# [Description("Tips")]
# [MessagePackObject(True)]
@dataclass
class TipMB(MasterBookBase):
    # [Description("Tipメッセージキー")]
    # [PropertyOrder(1)]
    MessageKey: str
    # [Description("遷移先")]
    # [PropertyOrder(2)]
    ViewTransitionType: ViewTransitionType
    # [Description("解放判定")]
    # [PropertyOrder(3)]
    OpenCommandType: OpenCommandType

# [Description("時差グループ")]
# [MessagePackObject(True)]
@dataclass
class TimeServerMB(MasterBookBase):
    # [Description("時差グループタイプ")]
    # [PropertyOrder(2)]
    TimeServerType: TimeServerType
    # [Description("国コードリスト")]
    # [PropertyOrder(6)]
    CountryCodeList: list[str]
    # [Description("デフォルト設定言語")]
    # [PropertyOrder(3)]
    DefaultLanguageType: LanguageType
    # [Description("デフォルト設定ボイス言語")]
    # [PropertyOrder(4)]
    DefaultVoiceLanguageType: LanguageType
    # [Description("表示名のキー")]
    # [PropertyOrder(5)]
    DisplayNameKey: str
    # [Description("時差グループ名")]
    # [PropertyOrder(1)]
    Name: str
    # [Description("UTCとの時差(例 01:00:00)")]
    # [PropertyOrder(2)]
    DifferenceDateTimeFromUtc: str

# [Description("テキストリソース")]
# [MessagePackObject(True)]
@dataclass
class TextResourceMB(MasterBookBase):
    # [Description("英語")]
    # [PropertyOrder(2)]
    enUS: str
    # [Description("日本語")]
    # [PropertyOrder(3)]
    jaJP: str
    # [Description("韓国語")]
    # [PropertyOrder(4)]
    koKR: str
    # [Description("文字列キー")]
    # [PropertyOrder(1)]
    StringKey: str
    # [Description("中国語(繁体字)")]
    # [PropertyOrder(6)]
    zhTW: str

# [Description("利用規約")]
# [MessagePackObject(True)]
@dataclass
class TermsMB(MasterBookBase):
    # [Description("TimeServerMBのID")]
    # [PropertyOrder(1)]
    TimeServerId: int
    # [Description("DMM用か？")]
    # [PropertyOrder(2)]
    IsDmm: bool
    # [Description("利用規約")]
    # [Nest(False, 0)]
    # [PropertyOrder(3)]
    Terms: TermsButtonInfo
    # [Description("プライバシーポリシー")]
    # [Nest(False, 0)]
    # [PropertyOrder(4)]
    PrivacyPolicy: TermsButtonInfo
    # [Description("サブスク規約")]
    # [Nest(False, 0)]
    # [PropertyOrder(5)]
    Subscription: TermsButtonInfo
    # [Description("その他")]
    # [Nest(False, 0)]
    # [PropertyOrder(6)]
    TermsButtonInfos: list[TermsButtonInfo]

# [Description("Steam商品価格表")]
# [MessagePackObject(True)]
@dataclass
class SteamProductPriceListMB(MasterBookBase):
    # [Description("JPYでの価格")]
    # [PropertyOrder(1)]
    JpyProductPrice: int
    # [Description("価格表")]
    # [Nest(False, 0)]
    # [PropertyOrder(2)]
    ProductPriceInfoList: list[SteamProductPriceInfo]

# [Description("国")]
# [MessagePackObject(True)]
@dataclass
class StateMB(MasterBookBase):
    # [Description("名称キー")]
    # [PropertyOrder(1)]
    NameKey: str
    # [Description("国ボーナスID")]
    # [PropertyOrder(6)]
    StateBonusId: int
    # [Description("サブ名称キー")]
    # [PropertyOrder(2)]
    SubNameKey: str
    # [Description("テキストキー")]
    # [PropertyOrder(3)]
    TextKey: str
    # [Description("クリファテキストキー")]
    # [PropertyOrder(4)]
    AppearQliphaKey: str
    # [Description("クリファテキストキー")]
    # [PropertyOrder(5)]
    AppearQliphaId: int
    # [Description("開始時間(JP)")]
    # [PropertyOrder(7)]
    BgmStartTimeJP: float
    # [Description("開始時間(US)")]
    # [PropertyOrder(8)]
    BgmStartTimeUS: float

# [Description("国ボーナス")]
# [MessagePackObject(True)]
@dataclass
class StateBonusMB(MasterBookBase):
    # [Description("時空の洞窟時空コインボーナス")]
    # [PropertyOrder(5)]
    DungeonCoinBonusPercent: int
    # [Description("ギルドバトルギルドコインボーナス")]
    # [PropertyOrder(6)]
    GuildCoinBonusPercent: int
    # [Description("曜日ボーナスが有効か")]
    # [PropertyOrder(4)]
    IsActiveWeeklyBonus: bool
    # [Description("国ボーナス表示アイテムアイコン情報")]
    # [Nest(False, 0)]
    # [PropertyOrder(2)]
    ItemIconInfo: ItemIconInfo
    # [Description("国ボーナス表示テキスト")]
    # [PropertyOrder(1)]
    StateBonusNameTextKey: str
    # [Description("国ボーナス表示数値")]
    # [PropertyOrder(3)]
    StateBonusNumberTextKey: str
    # [Description("累計貢献メダル報酬ボーナス情報")]
    # [Nest(True, 0)]
    # [PropertyOrder(7)]
    TotalActivityMedalRewardBonusList: list[TotalActivityMedalRewardBonus]

# [Description("スフィア")]
# [MessagePackObject(True)]
@dataclass
class SphereMB(MasterBookBase):
    # [Description("潜在能力変動情報")]
    # [Nest(False, 0)]
    # [PropertyOrder(7)]
    BaseParameterChangeInfo: BaseParameterChangeInfo
    # [Description("バトルパラメータ変動情報")]
    # [Nest(False, 0)]
    # [PropertyOrder(8)]
    BattleParameterChangeInfo: BattleParameterChangeInfo
    # [Description("スフィアの種類ID")]
    # [PropertyOrder(2)]
    CategoryId: int
    # [Description("説明文キー")]
    # [PropertyOrder(10)]
    DescriptionKey: str
    # [Description("攻撃系のスフィアか")]
    # [PropertyOrder(6)]
    IsAttackType: bool
    # [Description("スフィア強化に必要なアイテム")]
    # [Nest(False, 0)]
    # [PropertyOrder(9)]
    ItemListRequiredToCombine: list[UserItem]
    # [Description("スフィアレベル")]
    # [PropertyOrder(4)]
    Lv: int
    # [Description("名称キー")]
    # [PropertyOrder(1)]
    NameKey: str
    # [Description("レアリティ")]
    # [PropertyOrder(5)]
    RarityFlags: ItemRarityFlags
    # [Description("タイプId")]
    # [PropertyOrder(3)]
    SphereType: SphereType

# [Description("必要仮想通貨")]
# [MessagePackObject(True)]
@dataclass
class RequiredCurrencyMB(MasterBookBase):
    # [Description("ボス挑戦回数の購入に必要な仮想通貨")]
    # [PropertyOrder(3)]
    BossBattle: int
    # [Description("回数")]
    # [PropertyOrder(1)]
    Count: int
    # [Description("レジェンドリーグ挑戦回数に必要な仮想通貨")]
    # [PropertyOrder(5)]
    LegendLeague: int
    # [Description("PvP挑戦回数に必要な仮想通貨")]
    # [PropertyOrder(4)]
    Pvp: int
    # [Description("高速周回に必要な仮想通貨")]
    # [PropertyOrder(2)]
    Quick: int
    # [Description("訓練所挑戦回数の購入に必要な仮想通貨")]
    # [PropertyOrder(6)]
    TowerBattle: int
    # [Description("レベルリンク枠開放に必要な仮想通貨")]
    # [PropertyOrder(7)]
    LevelLinkMember: int

# [Description("クエスト")]
# [MessagePackObject(True)]
@dataclass
class QuestMB(MasterBookBase):
    # [Description("ベース戦闘力")]
    # [PropertyOrder(7)]
    BaseBattlePower: int
    # [Description("章ID")]
    # [MasterBookId(typeof)]
    # [PropertyOrder(1)]
    ChapterId: int
    # [Description("ゴールド(/m)")]
    # [PropertyOrder(3)]
    GoldPerMinute: int
    # [Description("最低獲得経験珠")]
    # [PropertyOrder(8)]
    MinCharacterExp: int
    # [Description("最低獲得プレイヤー経験値")]
    # [PropertyOrder(9)]
    MinPlayerExp: int
    # [Description("潜在宝珠(/d)")]
    # [PropertyOrder(4)]
    PotentialJewelPerDay: int
    # [Description("人口")]
    # [PropertyOrder(2)]
    Population: int
    # [Description("クエスト難易度")]
    # [PropertyOrder(6)]
    QuestDifficultyType: QuestDifficultyType
    # [Description("マップ建物ID")]
    # [PropertyOrder(5)]
    QuestMapBuildingId: int

# [Description("放置バトルマップオブジェクト")]
# [MessagePackObject(True)]
@dataclass
class QuestMapBuildingMB(MasterBookBase):
    # [Description("デフォルトタイプID")]
    # [PropertyOrder(1)]
    DefaultTypeId: int
    # [Description("選択タイプID 1")]
    # [PropertyOrder(2)]
    SelectTypeId1: int
    # [Description("選択タイプID 2")]
    # [PropertyOrder(3)]
    SelectTypeId2: int
    # [Description("選択タイプID 3")]
    # [PropertyOrder(4)]
    SelectTypeId3: int

# [Description("PVPランキング報酬")]
# [MessagePackObject(True)]
@dataclass
class PvpRankingRewardMB(MasterBookBase):
    # [Description("下限")]
    # [PropertyOrder(2)]
    LowerLimitRanking: int
    # [Description("PVPランキング報酬タイプ")]
    # [PropertyOrder(1)]
    PvpRankingRewardType: PvpRankingRewardType
    # [Description("報酬リスト")]
    # [Nest(False, 0)]
    # [PropertyOrder(4)]
    RewardList: list[UserItem]
    # [Description("上限")]
    # [PropertyOrder(3)]
    UpperLimitRanking: int

# [Description("プレイヤーランク")]
# [MessagePackObject(True)]
@dataclass
class PlayerRankMB(MasterBookBase):
    # [Description("キャラパラメータ攻撃力ボーナス")]
    # [PropertyOrder(4)]
    AttackPowerBonus: int
    # [Description("キャラパラメータクリティカルボーナス")]
    # [PropertyOrder(9)]
    CriticalBonus: int
    # [Description("キャラパラメータクリダメ強化ボーナス")]
    # [PropertyOrder(13)]
    CriticalDamageEnhanceBonus: int
    # [Description("キャラパラメータ物魔防御貫通ボーナス")]
    # [PropertyOrder(8)]
    DamageEnhanceBonus: int
    # [Description("キャラパラメータカウンタボーナス")]
    # [PropertyOrder(14)]
    DamageReflectBonus: int
    # [Description("キャラパラメータ弱体効果命中ボーナス")]
    # [PropertyOrder(11)]
    DebuffHitBonus: int
    # [Description("キャラパラメータ防御貫通ボーナス")]
    # [PropertyOrder(7)]
    DefensePenetrationBonus: int
    # [Description("キャラパラメータ命中ボーナス")]
    # [PropertyOrder(10)]
    HitBonus: int
    # [Description("キャラパラメータHPボーナス")]
    # [PropertyOrder(5)]
    HpBonus: int
    # [Description("キャラパラメータHP%ボーナス")]
    # [PropertyOrder(6)]
    HpPercentBonus: int
    # [Description("キャラパラメータHPドレインボーナス")]
    # [PropertyOrder(15)]
    HpDrainBonus: int
    # [Description("命中率ボーナス(パラメータX)")]
    # [PropertyOrder(16)]
    HitDirectPercentBonus: int
    # [Description("レベルリンク枠最大数")]
    # [PropertyOrder(17)]
    LevelLinkMemberMaxCount: int
    # [Description("ランク")]
    # [PropertyOrder(1)]
    Rank: int
    # [Description("必要累計経験値")]
    # [PropertyOrder(2)]
    RequiredTotalExp: int
    # [Description("解放時間")]
    # [PropertyOrder(3)]
    StartTimeFixJST: str
    # [Description("キャラパラメータスピードボーナス")]
    # [PropertyOrder(12)]
    SpeedBonus: int

# [Description("パッシブスキル")]
# [MessagePackObject(True)]
@dataclass
class PassiveSkillMB(MasterBookBase):
    # [Description("名称キー")]
    # [PropertyOrder(1)]
    NameKey: str
    # [Description("サブセットスキルリスト")]
    # [Nest(True, 1)]
    # [PropertyOrder(2)]
    PassiveSkillInfos: list[PassiveSkillInfo]

# [Description("コンテンツ開放")]
# [MessagePackObject(True)]
@dataclass
class OpenContentMB(MasterBookBase):
    # [Description("演出パス")]
    # [PropertyOrder(4)]
    AssetPath: str
    # [Description("開放内容キー")]
    # [PropertyOrder(3)]
    DescriptionKey: str
    # [Description("ガイド説明文")]
    # [PropertyOrder(8)]
    GuideDescriptionKey: str
    # [Description("ガイド表示優先順")]
    # [PropertyOrder(7)]
    GuideOrderNumber: int
    # [Description("ガイド表示タイプ")]
    # [PropertyOrder(6)]
    IsActiveGuide: bool
    # [Description("解放されるコマンドの種類")]
    # [PropertyOrder(5)]
    OpenCommandType: OpenCommandType
    # [Description("コンテンツ開放タイプ")]
    # [PropertyOrder(1)]
    OpenContentType: OpenContentType
    # [Description("コンテンツ開放値")]
    # [PropertyOrder(2)]
    OpenContentValue: int
    # [Description("トースト")]
    # [PropertyOrder(9)]
    ToastKey: str
    # [Description("トチュートリアルID")]
    # [PropertyOrder(10)]
    TutorialId: int

# [Description("新キャラミッション")]
# [MessagePackObject(True)]
@dataclass
class NewCharacterMissionMB(MasterBookBase):
    # [Description("開始日時")]
    # [PropertyOrder(1)]
    StartTimeFixJST: str
    # [Description("終了日時")]
    # [PropertyOrder(2)]
    EndTimeFixJST: str
    # [Description("強制開始時間")]
    # [PropertyOrder(3)]
    ForceStartTime: str
    # [Description("キャラ画像Id")]
    # [PropertyOrder(4)]
    CharacterImageId: int
    # [Description("キャラ画像座標X")]
    # [PropertyOrder(5)]
    CharacterImageX: float
    # [Description("キャラ画像座標Y")]
    # [PropertyOrder(6)]
    CharacterImageY: float
    # [Description("キャラ画像サイズ")]
    # [PropertyOrder(7)]
    CharacterImageSize: float
    # [Description("タイトル")]
    # [PropertyOrder(8)]
    TitleTextKey: str
    # [Description("対象ミッションID")]
    # [PropertyOrder(9)]
    TargetMissionIdList: list[int]
    # [Description("YouTube")]
    # [PropertyOrder(10)]
    YouTubeUrl: str
    # [Description("Twitter")]
    # [PropertyOrder(11)]
    TwitterUrl: str

# [Description("月間ログインボーナス報酬リスト")]
# [MessagePackObject(True)]
@dataclass
class MonthlyLoginBonusRewardListMB(MasterBookBase):
    # [Description("日別ログイン報酬リスト")]
    # [Nest(True, 1)]
    # [PropertyOrder(1)]
    DailyRewardList: list[LoginDailyRewardInfo]
    # [Description("合計ログイン報酬リスト")]
    # [Nest(True, 1)]
    # [PropertyOrder(2)]
    LoginCountRewardList: list[LoginCountRewardInfo]

# [Description("月間ログインボーナス")]
# [MessagePackObject(True)]
@dataclass
class MonthlyLoginBonusMB(MasterBookBase):
    # [Description("画像Id")]
    # [PropertyOrder(3)]
    ImageId: int
    # [Description("報酬リストID")]
    # [PropertyOrder(2)]
    RewardListId: int
    # [Description("年月")]
    # [PropertyOrder(1)]
    YearMonth: str

# [Description("ミッションタブ名")]
# [MessagePackObject(True)]
@dataclass
class MissionTabNameMB(MasterBookBase):
    # [Description("ミッション種別")]
    # [PropertyOrder(1)]
    MissionType: MissionType
    # [Description("ミッションタブ名")]
    # [PropertyOrder(2)]
    TabNameKey: str

# [Description("ミッション機能解放")]
# [MessagePackObject(True)]
@dataclass
class MissionOpenContentMB(MasterBookBase):
    # [Description("ミッションタイプ")]
    # [PropertyOrder(1)]
    AchievementType: MissionAchievementType
    # [Description("機能解放")]
    # [PropertyOrder(2)]
    OpenCommandType: OpenCommandType

# [Description("ミッション")]
# [MessagePackObject(True)]
@dataclass
class MissionMB(MasterBookBase):
    # [Description("ミッションタイプ")]
    # [PropertyOrder(6)]
    AchievementType: MissionAchievementType
    # [Description("ミッション説明")]
    # [PropertyOrder(4)]
    DescriptionKey: str
    # [Description("ミッション種別")]
    # [PropertyOrder(1)]
    MissionType: MissionType
    # [Description("ミッション名")]
    # [PropertyOrder(3)]
    NameKey: str
    # [Description("開放日数")]
    # [PropertyOrder(2)]
    OpeningPeriod: int
    # [Description("達成要求値")]
    # [PropertyOrder(7)]
    RequireValue: int
    # [Description("報酬リスト")]
    # [Nest(False, 0)]
    # [PropertyOrder(12)]
    RewardList: list[MissionReward]
    # [Description("表示優先度A")]
    # [PropertyOrder(10)]
    SortOrderA: int
    # [Description("表示優先度B")]
    # [PropertyOrder(11)]
    SortOrderB: int
    # [Description("遷移先")]
    # [PropertyOrder(5)]
    TransitionDestination: MissionTransitionDestinationType
    # [Description("終了時刻")]
    # [PropertyOrder(9)]
    EndTime: str
    # [Description("開始時刻")]
    # [PropertyOrder(8)]
    StartTime: str

# [Description("ミッションガイド")]
# [MessagePackObject(True)]
@dataclass
class MissionGuideMB(MasterBookBase):
    # [Description("ガイドID")]
    # [PropertyOrder(1)]
    GuideId: int
    # [Description("ミッションId")]
    # [PropertyOrder(2)]
    MissionId: int
    # [Description("ガイド表示優先度A")]
    # [PropertyOrder(5)]
    SortOrderA: int
    # [Description("ガイド表示優先度B")]
    # [PropertyOrder(6)]
    SortOrderB: int
    # [Description("ユーザ登録終了日時")]
    # [PropertyOrder(4)]
    EndTime: str
    # [Description("ユーザ登録開始日時")]
    # [PropertyOrder(3)]
    StartTime: str

# [Description("ミッションクリア個数報酬")]
# [MessagePackObject(True)]
@dataclass
class MissionClearCountRewardMB(MasterBookBase):
    # [Description("ミッション種別")]
    # [PropertyOrder(1)]
    MissionGroupType: MissionGroupType
    # [Description("必要クリア数")]
    # [PropertyOrder(2)]
    RequiredClearCount: int
    # [Description("報酬リスト")]
    # [Nest(False, 0)]
    # [PropertyOrder(3)]
    RewardList: list[MissionReward]

# [Description("幻影の神殿クエスト")]
# [MessagePackObject(True)]
@dataclass
class LocalRaidQuestMB(MasterBookBase):
    # [Description("初回報酬")]
    # [Nest(False, 0)]
    # [PropertyOrder(4)]
    FirstBattleRewards: list[UserItem]
    # [Description("通常報酬")]
    # [Nest(False, 0)]
    # [PropertyOrder(5)]
    FixedBattleRewards: list[UserItem]
    # [Description("敵Idリスト")]
    # [PropertyOrder(6)]
    LocalRaidEnemyIds: list[int]
    # [Description("レベル")]
    # [PropertyOrder(2)]
    Level: int
    # [Description("クエスト名キー")]
    # [PropertyOrder(1)]
    LocalRaidBannerId: int
    # [Description("個人戦力目安")]
    # [PropertyOrder(3)]
    RecommendedBattlePower: int

# [Description("幻影の神殿クエストグループ")]
# [MessagePackObject(True)]
@dataclass
class LocalRaidQuestGroupMB(MasterBookBase):
    # [Description("最大挑戦回数")]
    # [PropertyOrder(3)]
    MaxBattleCount: int
    # [Description("幻影の神殿Idグループリスト")]
    # [Nest(True, 0)]
    # [PropertyOrder(1)]
    LocalRaidQuestIdGroups: list[LocalRaidQuestIdGroup]
    # [Description("修練レベル")]
    # [PropertyOrder(2)]
    LocalRaidLevel: int
    # [Description("ワールド生成経過日数")]
    # [PropertyOrder(4)]
    OverDayFromCreateWorldTime: int

# [Description("幻影の神殿イベントスケジュール")]
# [MessagePackObject(True)]
@dataclass
class LocalRaidEventScheduleMB(MasterBookBase):
    # [Description("LocalRaidEventQuestGroupMBのIdリスト")]
    # [PropertyOrder(1)]
    LocalRaidEventQuestGroupIds: list[int]
    # [Description("イベントタイプ")]
    # [PropertyOrder(2)]
    LocalRaidEventType: LocalRaidEventType
    # [Description("報酬増加時間リスト")]
    # [Nest(False, 0)]
    # [PropertyOrder(3)]
    LocalRaidStartEndTimes: list[LocalRaidStartEndTime]
    # [Description("報酬増加倍率(100%=10000)")]
    # [PropertyOrder(4)]
    RewardBonusRate: int
    # [Description("開始日時")]
    # [PropertyOrder(5)]
    StartTime: str
    # [Description("終了日時")]
    # [PropertyOrder(6)]
    EndTime: str
    # [Description("イベントチュートリアルダイアログのID")]
    # [PropertyOrder(7)]
    LocalRaidEventTutorialId: int

# [Description("幻影の神殿イベントクエストグループ")]
# [MessagePackObject(True)]
@dataclass
class LocalRaidEventQuestGroupMB(MasterBookBase):
    # [Description("イベント追加挑戦回数")]
    # [PropertyOrder(4)]
    EventBattleCount: int
    # [Description("LocalRaidQuestMBのIdリスト")]
    # [PropertyOrder(1)]
    LocalRaidQuestIds: list[int]
    # [Description("修練レベル")]
    # [PropertyOrder(3)]
    LocalRaidLevel: int
    # [Description("イベント経過日数")]
    # [PropertyOrder(2)]
    OverDayFromStartEventTime: int
    # [Description("ワールド生成経過日数")]
    # [PropertyOrder(5)]
    OverDayFromCreateWorldTime: int

# [Description("幻影の神殿敵データ")]
# [MessagePackObject(True)]
@dataclass
class LocalRaidEnemyMB(MasterBookBase):
    # [Description("アクティブスキルIDのリスト")]
    # [PropertyOrder(12)]
    ActiveSkillIds: list[int]
    # [Description("ベースパラメータ")]
    # [Nest(True, 1)]
    # [PropertyOrder(9)]
    BaseParameter: BaseParameter
    # [Description("敵キャラクターID")]
    # [PropertyOrder(14)]
    BattleEnemyCharacterId: int
    # [Description("ユニットアイコンタイプ")]
    # [PropertyOrder(1)]
    UnitIconType: UnitIconType
    # [Description("ユニットアイコンID")]
    # [PropertyOrder(2)]
    UnitIconId: int
    # [Description("バトルパラメータ")]
    # [Nest(True, 1)]
    # [PropertyOrder(10)]
    BattleParameter: BattleParameter
    # [Description("戦闘力")]
    # [PropertyOrder(5)]
    BattlePower: int
    # [Description("職業")]
    # [PropertyOrder(6)]
    JobFlags: JobFlags
    # [Description("属性")]
    # [PropertyOrder(7)]
    ElementType: ElementType
    # [Description("レアリティ")]
    # [PropertyOrder(8)]
    CharacterRarityFlags: CharacterRarityFlags
    # [Description("敵のランク")]
    # [PropertyOrder(4)]
    EnemyRank: int
    # [Description("名称キー")]
    # [PropertyOrder(3)]
    NameKey: str
    # [Description("通常攻撃として使ってくるスキルID")]
    # [PropertyOrder(11)]
    NormalSkillId: int
    # [Description("パッシブスキルIDのリスト")]
    # [PropertyOrder(13)]
    PassiveSkillIds: list[int]
    # [Description("敵調整ID")]
    # [PropertyOrder(16)]
    EnemyAdjustId: int
    # [Description("敵武具ID")]
    # [PropertyOrder(15)]
    EnemyEquipmentId: int

# [Description("幻影の神殿バナー")]
# [MessagePackObject(True)]
@dataclass
class LocalRaidBannerMB(MasterBookBase):
    # [Description("クエスト名キー")]
    # [PropertyOrder(1)]
    NameKey: str
    # [Description("デコレーションID")]
    # [PropertyOrder(2)]
    DecorationId: int
    # [Description("デコレーション色")]
    # [PropertyOrder(3)]
    DecorationColor: str

# [Description("ローカル通知")]
# [MessagePackObject(True)]
@dataclass
class LocalPushNotificationMB(MasterBookBase):
    # [Description("グループID")]
    # [PropertyOrder(2)]
    GroupId: int
    # [Description("送信条件")]
    # [PropertyOrder(8)]
    LocalNotificationSendType: LocalNotificationSendType
    # [Description("通知タイプ")]
    # [PropertyOrder(1)]
    LocalNotificationType: LocalNotificationType
    # [Description("メッセージ")]
    # [PropertyOrder(7)]
    MessageKey: str
    # [Description("優先度")]
    # [PropertyOrder(5)]
    Priority: int
    # [Description("送信時刻")]
    # [PropertyOrder(9)]
    SendTime: str
    # [Description("タイトル")]
    # [PropertyOrder(6)]
    TitleKey: str
    # [Description("終了時間")]
    # [PropertyOrder(4)]
    EndTime: str
    # [Description("開始時間")]
    # [PropertyOrder(3)]
    StartTime: str

# [Description("ギルドバトル城")]
# [MessagePackObject(True)]
@dataclass
class LocalGvgCastleMB(MasterBookBase):
    # [Description("隣接する城のIDリスト")]
    # [PropertyOrder(3)]
    AdjacentCastleIds: list[int]
    # [Description("城タイプ")]
    # [PropertyOrder(2)]
    CastleType: CastleType
    # [Description("拠点報酬_固定")]
    # [Nest(False, 0)]
    # [PropertyOrder(4)]
    LocalGvgFixedRewards: list[UserItem]
    # [Description("拠点確率報酬ID")]
    # [PropertyOrder(5)]
    LotteryRewardId: int
    # [Description("名称キー")]
    # [PropertyOrder(1)]
    NameKey: str

# [Description("期間限定ミッション")]
# [MessagePackObject(True)]
@dataclass
class LimitedMissionMB(MasterBookBase):
    # [Description("開始日時")]
    # [PropertyOrder(1)]
    StartTime: str
    # [Description("終了日時")]
    # [PropertyOrder(2)]
    EndTime: str
    # [Description("キャラ画像Id")]
    # [PropertyOrder(3)]
    CharacterImageId: int
    # [Description("キャラ画像座標X")]
    # [PropertyOrder(4)]
    CharacterImageX: float
    # [Description("キャラ画像座標Y")]
    # [PropertyOrder(5)]
    CharacterImageY: float
    # [Description("キャラ画像サイズ")]
    # [PropertyOrder(6)]
    CharacterImageSize: float
    # [Description("タイトル")]
    # [PropertyOrder(7)]
    TitleTextKey: str
    # [Description("訴求文言")]
    # [PropertyOrder(8)]
    AppealTextKey: str
    # [Description("対象ミッションID")]
    # [PropertyOrder(9)]
    TargetMissionIdList: list[int]

# [Description("期間限定ログインボーナス報酬リスト")]
# [MessagePackObject(True)]
@dataclass
class LimitedLoginBonusRewardListMB(MasterBookBase):
    # [Description("日別報酬リスト")]
    # [Nest(False, 0)]
    # [PropertyOrder(1)]
    DailyRewardList: list[DailyLimitedLoginBonusItem]
    # [Description("毎日報酬")]
    # [Nest(False, 0)]
    # [PropertyOrder(3)]
    EveryDayRewardItem: EveryDayLimitedLoginBonusItem
    # [Description("毎日報酬有無")]
    # [PropertyOrder(2)]
    ExistEveryDayReward: bool
    # [Description("特別報酬有無")]
    # [PropertyOrder(4)]
    ExistSpecialReward: bool
    # [Description("特別報酬")]
    # [Nest(False, 0)]
    # [PropertyOrder(5)]
    SpecialRewardItem: SpecialLimitedLoginBonusItem

# [Description("期間限定ログインボーナス")]
# [MessagePackObject(True)]
@dataclass
class LimitedLoginBonusMB(MasterBookBase):
    # [Description("訴求文言")]
    # [PropertyOrder(8)]
    AppealTextKey: str
    # [Description("キャラ画像Id")]
    # [PropertyOrder(4)]
    CharacterImageId: int
    # [Description("報酬背景画像ID")]
    # [PropertyOrder(5)]
    RewardBackgroundImageId: int
    # [Description("報酬リストID")]
    # [PropertyOrder(3)]
    RewardListId: int
    # [Description("特別報酬訴求文言")]
    # [PropertyOrder(9)]
    SpecialRewardAppealTextKey: str
    # [Description("特別報酬背景画像ID")]
    # [PropertyOrder(6)]
    SpecialRewardBackgroundImageId: int
    # [Description("特別報酬カウントテキスト色")]
    # [PropertyOrder(12)]
    SpecialRewardCountTextColor: str
    # [Description("特別報酬ラベル色")]
    # [PropertyOrder(10)]
    SpecialRewardLabelTextColor: str
    # [Description("特別報酬ラベルアウトライン色")]
    # [PropertyOrder(11)]
    SpecialRewardLabelTextOutlineColor: str
    # [Description("タイトル")]
    # [PropertyOrder(7)]
    TitleTextKey: str
    # [Description("開始日時")]
    # [PropertyOrder(1)]
    StartTime: str
    # [Description("終了日時")]
    # [PropertyOrder(2)]
    EndTime: str

# [Description("期間限定イベント")]
# [MessagePackObject(True)]
@dataclass
class LimitedEventMB(MasterBookBase):
    # [Description("イベントの種類")]
    # [PropertyOrder(1)]
    LimitedEventType: LimitedEventType
    # [Description("開始日時")]
    # [PropertyOrder(2)]
    StartTime: str
    # [Description("終了日時")]
    # [PropertyOrder(3)]
    EndTime: str

# [Description("レベルリンク")]
# [MessagePackObject(True)]
@dataclass
class LevelLinkMB(MasterBookBase):
    # [Description("パーティーレベル")]
    PartyLevel: int
    # [Description("パーティーSubレベル")]
    PartySubLevel: int
    # [Description("レベルアップに必要なアイテム")]
    # [Nest(False, 0)]
    RequiredLevelUpItems: list[UserItem]

# [Description("レジェンドリーグ階級データ")]
# [MessagePackObject(True)]
@dataclass
class LegendLeagueClassMB(MasterBookBase):
    # [Description("階級名キー")]
    # [PropertyOrder(2)]
    ClassNameKey: str
    # [Description("レジェンドリーグ階級")]
    # [PropertyOrder(1)]
    ClassType: LegendLeagueClassType
    # [Description("最低必要ランク")]
    # [PropertyOrder(4)]
    RequiredMinimumRank: int
    # [Description("要求ポイント")]
    # [PropertyOrder(3)]
    RequiredPoint: int

# [Description("レビュー誘導用データ")]
# [MessagePackObject(True)]
@dataclass
class LeadReviewMB(MasterBookBase):
    # [Description("リセット日時")]
    # [PropertyOrder(1)]
    ResetDate: str

# [Description("アイテムの表示情報")]
# [MessagePackObject(True)]
@dataclass
class ItemMB(MasterBookBase):
    # [Description("説明文キー")]
    # [PropertyOrder(5)]
    DescriptionKey: str
    # [Description("表示名キー")]
    # [PropertyOrder(4)]
    DisplayName: str
    # [Description("終了時刻")]
    # [PropertyOrder(9)]
    EndTime: str
    # [Description("アイテムID")]
    # [PropertyOrder(2)]
    ItemId: int
    # [Description("レアリティ")]
    # [PropertyOrder(6)]
    ItemRarityFlags: ItemRarityFlags
    # [Description("アイテム種別")]
    # [PropertyOrder(1)]
    ItemType: ItemType
    # [Description("所持数上限")]
    # [PropertyOrder(10)]
    MaxItemCount: int
    # [Description("名称キー")]
    # [PropertyOrder(3)]
    NameKey: str
    # [Description("アイコンId")]
    # [PropertyOrder(11)]
    IconId: int
    # [Description("第2フレーム値")]
    # [PropertyOrder(14)]
    SecondaryFrameNum: int
    # [Description("第2フラーム種類")]
    # [PropertyOrder(13)]
    SecondaryFrameType: SecondaryFrameType
    # [Description("並び順（降順）")]
    # [PropertyOrder(7)]
    SortOrder: int
    # [Description("開始時刻")]
    # [PropertyOrder(8)]
    StartTime: str
    # [Description("遷移先ID")]
    # [PropertyOrder(12)]
    TransferSpotId: int

# [Description("お問い合わせボタン")]
# [MessagePackObject(True)]
@dataclass
class InquiryButtonMB(MasterBookBase):
    # [Description("ボタンテキスト")]
    # [PropertyOrder(1)]
    ButtonTextKey: str
    # [Description("ボタンタイプ")]
    # [PropertyOrder(2)]
    ButtonType: InquiryButtonType
    # [Description("メール本文キー")]
    # [PropertyOrder(4)]
    MailBodyKey: str
    # [Description("メール件名キー")]
    # [PropertyOrder(3)]
    MailSubjectKey: str
    # [Description("タイムサーバーID")]
    # [PropertyOrder(6)]
    TimeServerIds: list[int]
    # [Description("遷移先URL")]
    # [Nest(False, 0)]
    # [PropertyOrder(5)]
    TransferUrl: TranslatedText

# [Description("ヘルプ")]
# [MessagePackObject(True)]
@dataclass
class HelpMB(MasterBookBase):
    # [Description("ヘルプパートリスト")]
    # [Nest(False, 0)]
    # [PropertyOrder(2)]
    HelpPartInfoList: list[HelpPartInfo]
    # [Description("ヘルプタイトル")]
    # [PropertyOrder(1)]
    HelpTitle: str
    # [Description("表示フラグ")]
    # [PropertyOrder(4)]
    IsDisplayed: bool
    # [Description("チュートリアル説明ID")]
    # [PropertyOrder(3)]
    TutorialDescriptionId: int

# [Description("GvG修練レベル")]
# [MessagePackObject(True)]
@dataclass
class GvGServerLvMB(MasterBookBase):
    # [Description("経過日数")]
    # [PropertyOrder(2)]
    ElapsedDays: int
    # [Description("修練レベル")]
    # [PropertyOrder(1)]
    Lv: int
    # [Description("グランドバトル神殿上位最小配置数")]
    # [PropertyOrder(6)]
    MinCharacterNumGrandBattleLargeGolden: int
    # [Description("グランドバトル教会上位最小配置数")]
    # [PropertyOrder(7)]
    MinCharacterNumGrandBattleMediumGolden: int
    # [Description("グランドバトル城上位最小配置数")]
    # [PropertyOrder(8)]
    MinCharacterNumGrandBattleSmallGolden: int
    # [Description("グランドバトル神殿中位最小配置数")]
    # [PropertyOrder(9)]
    MinCharacterNumGrandBattleLargeSilver: int
    # [Description("グランドバトル教会中位最小配置数")]
    # [PropertyOrder(10)]
    MinCharacterNumGrandBattleMediumSilver: int
    # [Description("グランドバトル城中位最小配置数")]
    # [PropertyOrder(11)]
    MinCharacterNumGrandBattleSmallSilver: int
    # [Description("グランドバトル神殿下位最小配置数")]
    # [PropertyOrder(12)]
    MinCharacterNumGrandBattleLargeBronze: int
    # [Description("グランドバトル教会下位最小配置数")]
    # [PropertyOrder(13)]
    MinCharacterNumGrandBattleMediumBronze: int
    # [Description("グランドバトル城下位最小配置数")]
    # [PropertyOrder(14)]
    MinCharacterNumGrandBattleSmallBronze: int
    # [Description("ギルドバトル神殿最小配置数")]
    # [PropertyOrder(3)]
    MinCharacterNumGuildBattleLarge: int
    # [Description("ギルドバトル教会最小配置数")]
    # [PropertyOrder(4)]
    MinCharacterNumGuildBattleMedium: int
    # [Description("ギルドバトル城最小配置数")]
    # [PropertyOrder(5)]
    MinCharacterNumGuildBattleSmall: int

# [Description(" ギルドレイド報酬データ")]
# [MessagePackObject(True)]
@dataclass
class GuildRaidRewardMB(MasterBookBase):
    # [Description("ギルドダメージバー報酬リスト")]
    # [Nest(False, 0)]
    # [PropertyOrder(6)]
    GuildDamageBarRewards: list[GuildDamageBarReward]
    # [Description("一回の挑戦で獲得できるギルド経験値")]
    # [PropertyOrder(2)]
    GuildExpPerChallenge: int
    # [Description("ギルドレイドボスID")]
    # [PropertyOrder(1)]
    GuildRaidBossId: int
    # [Description("抽選報酬ID")]
    # [PropertyOrder(3)]
    LotteryRewardId: int
    # [Description("通常ダメージバー報酬リスト")]
    # [Nest(False, 0)]
    # [PropertyOrder(5)]
    NormalDamageBarRewards: list[NormalDamageBarReward]
    # [Description("武具Lvリスト")]
    # [Nest(False, 0)]
    # [PropertyOrder(4)]
    QuestClearEquipmentLvList: list[GuildRaidQuestClearEquipmentLvList]
    # [Description("ワールド報酬目標リスト")]
    # [Nest(False, 0)]
    # [PropertyOrder(7)]
    WorldDamageBarRewards: list[WorldDamageBarReward]
    # [Description("非表示ワールドダメージ")]
    # [PropertyOrder(8)]
    HideWorldDamage: int

# [Description(" ギルドレイドボスデータ")]
# [MessagePackObject(True)]
@dataclass
class GuildRaidBossMB(MasterBookBase):
    # [Description("アクティブスキルIDのリスト")]
    # [PropertyOrder(17)]
    ActiveSkillIds: list[int]
    # [Description("ベースパラメータ")]
    # [Nest(True, 1)]
    # [PropertyOrder(14)]
    BaseParameter: BaseParameter
    # [Description("バトルパラメータ")]
    # [Nest(True, 1)]
    # [PropertyOrder(15)]
    BattleParameter: BattleParameter
    # [Description("戦闘力")]
    # [PropertyOrder(12)]
    BattlePower: int
    # [Description("レアリティ")]
    # [PropertyOrder(13)]
    CharacterRarityFlags: CharacterRarityFlags
    # [Description("属性")]
    # [PropertyOrder(10)]
    ElementType: ElementType
    # [Description("敵のランク")]
    # [PropertyOrder(8)]
    EnemyRank: int
    # [Description("ギルドダメージバー")]
    # [Nest(False, 0)]
    # [PropertyOrder(20)]
    GuildDamageBar: list[GuildRaidDamageBar]
    # [Description("ボス種別")]
    # [PropertyOrder(3)]
    GuildRaidBossType: GuildRaidBossType
    # [Description("職業")]
    # [PropertyOrder(11)]
    JobFlags: JobFlags
    # [Description("名称キー")]
    # [PropertyOrder(9)]
    NameKey: str
    # [Description("通常ダメージバー")]
    # [Nest(False, 0)]
    # [PropertyOrder(19)]
    NormalDamageBar: list[GuildRaidDamageBar]
    # [Description("通常攻撃として使ってくるスキルID")]
    # [PropertyOrder(16)]
    NormalSkillId: int
    # [Description("パッシブスキルIDのリスト")]
    # [PropertyOrder(18)]
    PassiveSkillIds: list[int]
    # [Description("必要ギルド貢献値")]
    # [PropertyOrder(6)]
    ReleasableGuildFame: int
    # [Description("ユニットアイコンID")]
    # [PropertyOrder(2)]
    UnitIconId: int
    # [Description("ユニットアイコンタイプ")]
    # [PropertyOrder(1)]
    UnitIconType: UnitIconType
    # [Description("開始日時（現地時間）")]
    # [PropertyOrder(4)]
    StartTime: str
    # [Description("終了日時（現地時間")]
    # [PropertyOrder(5)]
    EndTime: str
    # [Description("キャラクター座標X")]
    # [PropertyOrder(21)]
    CharacterImageX: float
    # [Description("キャラクター座標Y")]
    # [PropertyOrder(22)]
    CharacterImageY: float
    # [Description("バナーテキスト")]
    # [PropertyOrder(23)]
    BannerText: str
    # [Description("ギルドレイドボタン座標U")]
    # [PropertyOrder(24)]
    GuildRaidButtonU: float
    # [Description("ギルドレイドボタン座標V")]
    # [PropertyOrder(25)]
    GuildRaidButtonV: float

# [Description("ギルドレベル")]
# [MessagePackObject(True)]
@dataclass
class GuildLevelMB(MasterBookBase):
    # [Description("1日の経験値獲得上限")]
    # [PropertyOrder(4)]
    DayLimitExp: int
    # [Description("レベル")]
    # [PropertyOrder(1)]
    Level: int
    # [Description("加入可能人数")]
    # [PropertyOrder(2)]
    NumberOfPossibleJoinPeople: int
    # [Description("必要累計経験値")]
    # [PropertyOrder(3)]
    RequiredTotalExp: int

# [Description("グランドバトル城")]
# [MessagePackObject(True)]
@dataclass
class GlobalGvgCastleMB(MasterBookBase):
    # [Description("隣接する城のIDリスト")]
    # [PropertyOrder(4)]
    AdjacentCastleIds: list[int]
    # [Description("拠点ポイント")]
    # [PropertyOrder(3)]
    CastlePoint: int
    # [Description("城タイプ")]
    # [PropertyOrder(2)]
    CastleType: CastleType
    # [Description("拠点報酬_固定")]
    # [Nest(True, 0)]
    # [PropertyOrder(5)]
    GlobalGvgFixedRewards: GlobalGvgFixedRewards
    # [Description("抽選報酬ID")]
    # [PropertyOrder(6)]
    LotteryRewardId: int
    # [Description("名称キー")]
    # [PropertyOrder(1)]
    NameKey: str

# [Description("ガチャセレクトリスト")]
# [MessagePackObject(True)]
@dataclass
class GachaSelectListMB(MasterBookBase):
    # [Description("設定可能キャラクターIDリスト")]
    # [PropertyOrder(5)]
    CharacterIdList: list[int]
    # [Description("ガチャセレクトリストタイプ")]
    # [PropertyOrder(1)]
    GachaSelectListType: GachaSelectListType
    # [Description("新規キャラクターIDリスト")]
    # [PropertyOrder(6)]
    NewCharacterIdList: list[int]
    # [Description("優先度")]
    # [PropertyOrder(4)]
    OrderNumber: int
    # [Description("開始時間(JST)")]
    # [PropertyOrder(2)]
    StartTimeFixJST: str
    # [Description("終了時間(JST)")]
    # [PropertyOrder(3)]
    EndTimeFixJST: str

# [Description("運命ガチャ追加キャラクター")]
# [MessagePackObject(True)]
@dataclass
class GachaDestinyAddCharacterMB(MasterBookBase):
    # [Description("キャラクターID")]
    # [PropertyOrder(1)]
    CharacterId: int
    # [Description("セレクトリスト追加タイプ")]
    # [PropertyOrder(2)]
    GachaAddCharacterType: GachaAddCharacterType
    # [Description("開始時間参照用GachaSelectListMBのID")]
    # [PropertyOrder(3)]
    StartGachaSelectListId: int
    # [Description("終了時間参照用GachaSelectListMBのID")]
    # [PropertyOrder(4)]
    EndGachaSelectListId: int

# [Description("ガチャ筐体描画用")]
# [MessagePackObject(True)]
@dataclass
class GachaCaseUiMB(MasterBookBase):
    # [Description("バナー")]
    # [Nest(False, 0)]
    # [PropertyOrder(1)]
    Banner: TranslatedText
    # [Description("バナー画像番号")]
    # [PropertyOrder(13)]
    BannerImageNumber: int
    # [Description("レイアウト")]
    # [Nest(False, 0)]
    # [PropertyOrder(12)]
    CustomTextLayout: CustomTextLayout
    # [Description("詳細ダイアログ 詳細")]
    # [Nest(False, 0)]
    # [PropertyOrder(18)]
    DetailDialogDetail: TranslatedText
    # [Description("詳細ダイアログ 見出し")]
    # [Nest(False, 0)]
    # [PropertyOrder(17)]
    DetailDialogHeading: TranslatedText
    # [Description("詳細ダイアログ 注意")]
    # [Nest(False, 0)]
    # [PropertyOrder(19)]
    DetailDialogNotes: TranslatedText
    # [Description("ガチャ詳細URL")]
    # [Nest(False, 0)]
    # [PropertyOrder(6)]
    DetailURL: TranslatedText
    # [Description("武具図鑑タブ番号")]
    # [PropertyOrder(15)]
    EquipmentPictureBookTabIndex: int
    # [Description("説明補足")]
    # [Nest(False, 0)]
    # [PropertyOrder(3)]
    Explanation: TranslatedText
    # [Description("ボーナスゲージタイプ")]
    # [PropertyOrder(16)]
    GachaBonusGaugeType: GachaBonusGaugeType
    # [Description("ボタンメッセージキー")]
    # [Nest(False, 0)]
    # [PropertyOrder(7)]
    GachaButtonMessage: TranslatedText
    # [Description("ヘッダーアイテム1")]
    # [Nest(False, 0)]
    # [PropertyOrder(8)]
    HeaderItem1: UserItem
    # [Description("ヘッダーアイテム2")]
    # [Nest(False, 0)]
    # [PropertyOrder(9)]
    HeaderItem2: UserItem
    # [Description("ヘッダーアイテム3")]
    # [Nest(False, 0)]
    # [PropertyOrder(10)]
    HeaderItem3: UserItem
    # [Description("回数報酬表示")]
    # [PropertyOrder(11)]
    IsLotteryViewShowBonusItem: bool
    # [Description("タイトル")]
    # [Nest(False, 0)]
    # [PropertyOrder(2)]
    Name: TranslatedText
    # [Description("ピックアップされるキャラクター")]
    # [PropertyOrder(4)]
    PickUpCharacterId: int
    # [Description("時間テキスト")]
    # [Nest(False, 0)]
    # [PropertyOrder(14)]
    TimeFormat: TranslatedText
    # [Description("タイトル色")]
    # [PropertyOrder(5)]
    TitleColorType: GachaTitleColorType
    # [Description("追加報酬アイテム")]
    # [Nest(False, 0)]
    # [PropertyOrder(20)]
    AddRewardItems: list[UserItem]
    # [Description("天井テキスト")]
    # [PropertyOrder(21)]
    CeilingCountFormatKey: str

# [Description("ガチャ筐体")]
# [MessagePackObject(True)]
@dataclass
class GachaCaseMB(MasterBookBase):
    # [Description("表示順(降順)")]
    # [PropertyOrder(3)]
    DisplayOrder: int
    # [Description("属性(属性ガチャ用)")]
    # [PropertyOrder(5)]
    ElementType: ElementType
    # [Description("GachaCaseUiMBのID")]
    # [PropertyOrder(1)]
    GachaCaseUiId: int
    # [Description("カテゴリー")]
    # [PropertyOrder(2)]
    GachaCategoryType: GachaCategoryType
    # [Description("運命(運命ガチャ用)")]
    # [PropertyOrder(7)]
    GachaDestinyType: GachaDestinyType
    # [Description("ガチャグループタイプ")]
    # [PropertyOrder(4)]
    GachaGroupType: GachaGroupType
    # [Description("聖遺物(聖天使の信託ガチャ用)")]
    # [PropertyOrder(6)]
    GachaRelicType: GachaRelicType
    # [Description("表示用残り時間初期化タイプ")]
    # [PropertyOrder(9)]
    GachaResetType: GachaResetType
    # [Description("セレクトリストタイプ")]
    # [PropertyOrder(8)]
    GachaSelectListType: GachaSelectListType
    # [Description("ガチャ天井表示用フラグ")]
    # [PropertyOrder(10)]
    GachaCaseFlags: GachaCaseFlags
    # [Description("ガチャの日数制限(プレイヤー生成時から計算、０は無視)")]
    # [PropertyOrder(13)]
    GachaLimitDayFromCreatePlayer: int
    # [Description("新ガチャの開始時間(JST)")]
    # [PropertyOrder(11)]
    StartTimeFixJST: str
    # [Description("新ガチャの終了時間(JST)")]
    # [PropertyOrder(12)]
    EndTimeFixJST: str

# [Description("フレンドミッション")]
# [MessagePackObject(True)]
@dataclass
class FriendMissionMB(MasterBookBase):
    # [Description("ミッション名")]
    # [PropertyOrder(1)]
    NameKey: str
    # [Description("遷移先")]
    # [PropertyOrder(2)]
    TransitionDestination: MissionTransitionDestinationType
    # [Description("ミッションタイプ")]
    # [PropertyOrder(3)]
    AchievementType: MissionAchievementType
    # [Description("達成要求値")]
    # [PropertyOrder(4)]
    RequireValue: int
    # [Description("表示優先度")]
    # [PropertyOrder(7)]
    SortOrder: int
    # [Description("報酬リスト")]
    # [Nest(False, 0)]
    # [PropertyOrder(8)]
    RewardList: list[UserItem]
    # [Description("終了時刻")]
    # [PropertyOrder(6)]
    EndTime: str
    # [Description("開始時刻")]
    # [PropertyOrder(5)]
    StartTime: str

# [Description("フレンドキャンペーン")]
# [MessagePackObject(True)]
@dataclass
class FriendCampaignMB(MasterBookBase):
    # [Description("コード入力有効期間")]
    # [PropertyOrder(3)]
    CodeExpirationPeriod: int
    # [Description("招待コード入力上限数")]
    # [PropertyOrder(10)]
    CodeLimitCount: int
    # [Description("対象フレンドミッションリスト")]
    # [PropertyOrder(8)]
    FriendMissionIdList: list[int]
    # [Description("招待コード入力報酬リスト")]
    # [Nest(False, 0)]
    # [PropertyOrder(11)]
    RewardItemList: list[UserItem]
    # [Description("キャンペーンタイトル")]
    # [PropertyOrder(9)]
    Title: str
    # [Description("キャラ画像Id")]
    # [PropertyOrder(4)]
    CharacterImageId: int
    # [Description("キャラ画像座標X")]
    # [PropertyOrder(5)]
    CharacterImageX: float
    # [Description("キャラ画像座標Y")]
    # [PropertyOrder(6)]
    CharacterImageY: float
    # [Description("キャラ画像サイズ")]
    # [PropertyOrder(7)]
    CharacterImageSize: float
    # [Description("終了時刻")]
    # [PropertyOrder(2)]
    EndTime: str
    # [Description("開始時刻")]
    # [PropertyOrder(1)]
    StartTime: str

# [Description("よくある質問リスト")]
# [MessagePackObject(True)]
@dataclass
class FaqListMB(MasterBookBase):
    # [Description("質問項目タイトルKey")]
    # [PropertyOrder(1)]
    QuestionTitleKey: str
    # [Description("遷移先URL")]
    # [Nest(False, 0)]
    # [PropertyOrder(2)]
    TransferUrl: TranslatedText

# [Description("APIエラーコード")]
# [MessagePackObject(True)]
@dataclass
class ErrorCodeMB(MasterBookBase):
    # [Description("メッセージタイプ")]
    # [PropertyOrder(1)]
    ErrorMessageType: ErrorMessageType

# [Description("武具セット")]
# [MessagePackObject(True)]
@dataclass
class EquipmentSetMB(MasterBookBase):
    # [Description("セット効果リスト")]
    # [Nest(False, 0)]
    # [PropertyOrder(2)]
    EffectList: list[EquipmentSetEffect]
    # [Description("名称キー")]
    # [PropertyOrder(1)]
    NameKey: str

# [Description("武具進化素材")]
# [MessagePackObject(True)]
@dataclass
class EquipmentSetMaterialMB(MasterBookBase):
    # [Description("説明文キー")]
    # [PropertyOrder(4)]
    DescriptionKey: str
    # [Description("アイコンID")]
    # [PropertyOrder(5)]
    IconId: int
    # [Description("レアリティ")]
    # [PropertyOrder(7)]
    ItemRarityFlags: ItemRarityFlags
    # [Description("レベル")]
    # [PropertyOrder(3)]
    Lv: int
    # [Description("名称キー")]
    # [PropertyOrder(1)]
    NameKey: str
    # [Description("表示名キー")]
    # [PropertyOrder(2)]
    DisplayNameKey: str
    # [Description("入手ステージ Quest ID")]
    # [PropertyOrder(6)]
    QuestIdList: list[int]

# [Description("武具強化パラメータテーブル")]
# [MessagePackObject(True)]
@dataclass
class EquipmentReinforcementParameterMB(MasterBookBase):
    # [Description("強化倍率係数")]
    # [PropertyOrder(1)]
    ReinforcementCoefficient: float

# [Description("武具強化アイテムテーブル")]
# [MessagePackObject(True)]
@dataclass
class EquipmentReinforcementMaterialMB(MasterBookBase):
    # [Description("レベル毎の強化アイテムリスト")]
    # [Nest(False, 0)]
    # [PropertyOrder(1)]
    ReinforcementMap: list[EquipmentReinforcementMaterialInfo]

# [Description("武具")]
# [MessagePackObject(True)]
@dataclass
class EquipmentMB(MasterBookBase):
    # [Description("付加パラメータ合計値")]
    # [PropertyOrder(10)]
    AdditionalParameterTotal: int
    # [Description("進化先武具ID")]
    # [PropertyOrder(16)]
    AfterLevelEvolutionEquipmentId: int
    # [Description("進化先レアリティ武具ID")]
    # [PropertyOrder(17)]
    AfterRarityEvolutionEquipmentId: int
    # [Description("基礎パラメータ")]
    # [Nest(False, 0)]
    # [PropertyOrder(9)]
    BattleParameterChangeInfo: BattleParameterChangeInfo
    # [Description("武具カテゴリ")]
    # [PropertyOrder(7)]
    Category: EquipmentCategory
    # [Description("合成情報ID")]
    # [PropertyOrder(19)]
    CompositeId: int
    # [Description("武具進化テーブルID")]
    # [PropertyOrder(18)]
    EquipmentEvolutionId: int
    # [Description("専属スキル説明文ID")]
    # [PropertyOrder(15)]
    EquipmentExclusiveSkillDescriptionId: int
    # [Description("鋳造ID")]
    # [PropertyOrder(21)]
    EquipmentForgeId: int
    # [Description("武具レベル")]
    # [PropertyOrder(3)]
    EquipmentLv: int
    # [Description("武具強化素材テーブルID")]
    # [PropertyOrder(12)]
    EquipmentReinforcementMaterialId: int
    # [Description("武具セットID")]
    # [PropertyOrder(13)]
    EquipmentSetId: int
    # [Description("装備可能キャラタイプ")]
    # [PropertyOrder(6)]
    EquippedJobFlags: JobFlags
    # [Description("専属効果ID")]
    # [PropertyOrder(14)]
    ExclusiveEffectId: int
    # [Description("最初の宝石スロット解放に必要な銅貨")]
    # [PropertyOrder(23)]
    GoldRequiredToOpeningFirstSphereSlot: int
    # [Description("ロック無し鍛錬に必要な銅貨")]
    # [PropertyOrder(22)]
    GoldRequiredToTraining: int
    # [Description("アイコンID")]
    # [PropertyOrder(24)]
    IconId: int
    # [Description("名称キー")]
    # [PropertyOrder(1)]
    NameKey: str
    # [Description("装備評価")]
    # [PropertyOrder(4)]
    PerformancePoint: int
    # [Description("品質レベル")]
    # [PropertyOrder(8)]
    QualityLv: int
    # [Description("レアリティ")]
    # [PropertyOrder(2)]
    RarityFlags: EquipmentRarityFlags
    # [Description("武具の装備枠タイプ")]
    # [PropertyOrder(5)]
    SlotType: EquipmentSlotType

# [Description("魔装テーブル")]
# [MessagePackObject(True)]
@dataclass
class EquipmentMatchlessSacredTreasureMB(MasterBookBase):
    # [Description("メイル：防御貫通（加算式増加）")]
    # [PropertyOrder(7)]
    ArmorDefensePenetration: int
    # [Description("アーム：魔法防御（加算式増加）")]
    # [PropertyOrder(5)]
    GauntletMagicDamageRelax: int
    # [Description("メット：クリティカル（加算式増加）")]
    # [PropertyOrder(6)]
    HelmetCritical: int
    # [Description("魔装レベル")]
    # [PropertyOrder(1)]
    Lv: int
    # [Description("必要累積経験値")]
    # [PropertyOrder(2)]
    RequiredTotalExp: int
    # [Description("ブーツ：HP（加算式増加）")]
    # [PropertyOrder(8)]
    ShoesHp: int
    # [Description("アクセサリ：物理防御（加算式増加）")]
    # [PropertyOrder(4)]
    SubPhysicalDamageRelax: int
    # [Description("武器：攻撃力（加算式増加）")]
    # [PropertyOrder(3)]
    WeaponAttackPower: int

# [Description("聖装テーブル")]
# [MessagePackObject(True)]
@dataclass
class EquipmentLegendSacredTreasureMB(MasterBookBase):
    # [Description("メイル：魔法クリティカル抵抗（加算式増加）")]
    # [PropertyOrder(7)]
    ArmorMagicCriticalDamageRelaxPercent: float
    # [Description("アーム：クリティカルダメージ（加算式増加）")]
    # [PropertyOrder(5)]
    GauntletCriticalDamagePercent: float
    # [Description("メット：物理クリティカル抵抗（加算式増加）")]
    # [PropertyOrder(6)]
    HelmetPhysicalCriticalDamageRelaxPercent: float
    # [Description("聖装レベル")]
    # [PropertyOrder(1)]
    Lv: int
    # [Description("必要累積経験値")]
    # [PropertyOrder(2)]
    RequiredTotalExp: int
    # [Description("ブーツ：HPドレイン（加算式増加）")]
    # [PropertyOrder(8)]
    ShoesHpDrainPercent: float
    # [Description("アクセサリー：命中（割合増加）")]
    # [PropertyOrder(4)]
    SubHitPercent: float
    # [Description("武器：攻撃力（割合増加）")]
    # [PropertyOrder(3)]
    WeaponAttackPowerPercent: float

# [Description("鋳造データ")]
# [MessagePackObject(True)]
@dataclass
class EquipmentForgeMB(MasterBookBase):
    # [Description("魔装ステータス")]
    # [PropertyOrder(3)]
    MatchlessSacredTreasure: bool
    # [Description("得られる鋳造値")]
    # [PropertyOrder(4)]
    PriceForForge: int
    # [Description("成功時の武具レアリティ")]
    # [PropertyOrder(2)]
    SuccessRarityFlag: EquipmentRarityFlags
    # [Description("成功率ID")]
    # [PropertyOrder(1)]
    SuccessRateId: int

# [Description("専属スキル説明文")]
# [MessagePackObject(True)]
@dataclass
class EquipmentExclusiveSkillDescriptionMB(MasterBookBase):
    # [Description("説明文1キー")]
    # [PropertyOrder(1)]
    Description1Key: str
    # [Description("説明文2キー")]
    # [PropertyOrder(2)]
    Description2Key: str
    # [Description("説明文3キー")]
    # [PropertyOrder(3)]
    Description3Key: str

# [Description("武具専属効果")]
# [MessagePackObject(True)]
@dataclass
class EquipmentExclusiveEffectMB(MasterBookBase):
    # [Description("専属効果(BaseParameter)")]
    # [Nest(False, 0)]
    # [PropertyOrder(2)]
    BaseParameterChangeInfoList: list[BaseParameterChangeInfo]
    # [Description("専属効果(BattleParameter)")]
    # [Nest(False, 0)]
    # [PropertyOrder(3)]
    BattleParameterChangeInfoList: list[BattleParameterChangeInfo]
    # [Description("専属効果適用キャラクターID")]
    # [PropertyOrder(1)]
    CharacterId: int

# [Description("武具進化テーブル")]
# [MessagePackObject(True)]
@dataclass
class EquipmentEvolutionMB(MasterBookBase):
    # [Description("必要アイテム情報")]
    # [Nest(False, 0)]
    # [PropertyOrder(1)]
    EquipmentEvolutionInfoList: list[EquipmentEvolutionInfo]
    # [Description("武具進化の種類")]
    # [PropertyOrder(2)]
    EvolutionType: EvolutionType

# [Description("武具合成")]
# [MessagePackObject(True)]
@dataclass
class EquipmentCompositeMB(MasterBookBase):
    # [Description("合成した際に取得する武具ID")]
    # [PropertyOrder(1)]
    EquipmentId: int
    # [Description("レアリティ")]
    # [PropertyOrder(4)]
    ItemRarityFlags: ItemRarityFlags
    # [Description("必要欠片数")]
    # [PropertyOrder(2)]
    RequiredFragmentCount: int
    # [Description("必要アイテム情報")]
    # [Nest(False, 0)]
    # [PropertyOrder(3)]
    RequiredItemList: list[UserItem]

# [Description("属性ボーナス")]
# [MessagePackObject(True)]
@dataclass
class ElementBonusMB(MasterBookBase):
    # [Description("増加パラメータリスト")]
    # [Nest(False, 0)]
    # [PropertyOrder(3)]
    BattleParameterChangeInfos: list[BattleParameterChangeInfo]
    # [Description("属性条件タイプ")]
    # [PropertyOrder(1)]
    ConditionType: ElementBonusConditionType
    # [Description("発動段階")]
    # [PropertyOrder(2)]
    Phase: ElementBonusPhaseType

# [Description("スキル効果グループ")]
# [MessagePackObject(True)]
@dataclass
class EffectGroupMB(MasterBookBase):
    # [Description("付与者アイコンID")]
    # [PropertyOrder(6)]
    CasterIconId: int
    # [Description("付与者アイコンタイプ")]
    # [PropertyOrder(5)]
    CasterIconType: EffectGroupIconType
    # [Description("説明文キー")]
    # [PropertyOrder(2)]
    DescriptionKey: str
    # [Description("効果アイコンID")]
    # [PropertyOrder(4)]
    IconId: int
    # [Description("効果アイコンタイプ")]
    # [PropertyOrder(3)]
    IconType: EffectGroupIconType
    # [Description("効果名キー")]
    # [PropertyOrder(1)]
    NameKey: str
    # [Description("強制非表示フラグ")]
    # [PropertyOrder(7)]
    IsHide: bool
    # [Description("ターン数非表示フラグ")]
    # [PropertyOrder(8)]
    IsTurnHide: bool

# [Description("時空の洞窟 加護")]
# [MessagePackObject(True)]
@dataclass
class DungeonBattleRelicMB(MasterBookBase):
    # [Description("戦闘力ボーナス")]
    # [PropertyOrder(4)]
    BattlePowerBonus: int
    # [Description("戦闘力ボーナス対象")]
    # [PropertyOrder(5)]
    BattlePowerBonusTargetType: DungeonBattleRelicBattlePowerBonusTargetType
    # [Description("複数所持可能有無")]
    # [PropertyOrder(6)]
    CanMultiplePossession: bool
    # [Description("説明文キー")]
    # [PropertyOrder(8)]
    DescriptionKey: str
    # [Description("レアリティ")]
    # [PropertyOrder(2)]
    DungeonRelicRarityType: DungeonBattleRelicRarityType
    # [Description("名前キー")]
    # [PropertyOrder(1)]
    NameKey: str
    # [Description("パッシブスキルタイプ情報")]
    # [Nest(False, 0)]
    # [PropertyOrder(7)]
    PassiveSkillTypeInfos: list[PassiveSkillTypeInfo]
    # [Description("下位ID（0の場合は直接入手可能）")]
    # [PropertyOrder(3)]
    ReinforceFrom: int
    # [Description("アイコンID")]
    # [PropertyOrder(9)]
    IconId: int

# [Description("時空の洞窟 アシストキャラクター")]
# [MessagePackObject(True)]
@dataclass
class DungeonBattleGuestMB(MasterBookBase):
    # [Description("キャラクターID")]
    # [PropertyOrder(1)]
    CharacterId: int
    # [Description("優先的に出現させるか")]
    # [PropertyOrder(2)]
    IsPickup: bool
    # [Description("優先出現終了時間(JST)")]
    # [PropertyOrder(4)]
    EndTimeFixJST: str
    # [Description("優先出現開始時間(JST)")]
    # [PropertyOrder(3)]
    StartTimeFixJST: str

# [Description("時空の洞窟 マス詳細")]
# [MessagePackObject(True)]
@dataclass
class DungeonBattleGridMB(MasterBookBase):
    # [Description("マス名キー")]
    # [PropertyOrder(1)]
    DungeonGridNameKey: str
    # [Description("マス種別")]
    # [PropertyOrder(2)]
    DungeonGridType: DungeonBattleGridType

# [Description("ディープリンク")]
# [MessagePackObject(True)]
@dataclass
class DeepLinkMB(MasterBookBase):
    # [Description("遷移タイプ")]
    # [Nest(False, 0)]
    # [PropertyOrder(1)]
    TransferDetailInfo: TransferDetailInfo

# [Description("コミュニティ")]
# [MessagePackObject(True)]
@dataclass
class CommunityMB(MasterBookBase):
    # [Description("地域タイプ")]
    # [PropertyOrder(1)]
    CountryCodeType: CountryCodeType
    # [Description("SNS情報リスト")]
    # [Nest(False, 0)]
    # [PropertyOrder(2)]
    SnsInfoList: list[SnsInfo]

# [Description("回想テーブル")]
# [MessagePackObject(True)]
@dataclass
class CharacterStoryMB(MasterBookBase):
    # [Description("対象キャラクターID")]
    # [PropertyOrder(1)]
    CharacterId: int
    # [Description("何個目の回想か")]
    # [PropertyOrder(2)]
    EpisodeId: int
    # [Description("制限レベル")]
    # [PropertyOrder(3)]
    Level: int
    # [Description("制限レアリティ")]
    # [PropertyOrder(7)]
    RarityFlags: CharacterRarityFlags
    # [Description("初閲覧時報酬")]
    # [Nest(False, 0)]
    # [PropertyOrder(5)]
    RewardItemList: list[UserItem]
    # [Description("スキップ説明文")]
    # [PropertyOrder(6)]
    TextKey: str
    # [Description("タイトルキー")]
    # [PropertyOrder(4)]
    TitleKey: str

# [Description("キャラクターリセット")]
# [MessagePackObject(True)]
@dataclass
class CharacterResetMB(MasterBookBase):
    # [Description("リセット対象のレアリティ")]
    # [PropertyOrder(2)]
    CharacterRarityFlags: CharacterRarityFlags
    # [Description("リセット対象の属性の分類")]
    # [PropertyOrder(1)]
    ElementClassificationType: ElementClassificationType
    # [Description("同名のSR+のLv1キャラ返還数")]
    # [PropertyOrder(3)]
    ReturnCharacterCount: int
    # [Description("魔女の手紙返還数")]
    # [PropertyOrder(4)]
    ReturnWitchLetterCount: int

# [Description("キャラクターランクアップ")]
# [MessagePackObject(True)]
@dataclass
class CharacterRankUpMaterialMB(MasterBookBase):
    # [Description("属性の分類")]
    # [PropertyOrder(1)]
    ElementClassification: ElementClassificationType
    # [Description("Material")]
    # [PropertyOrder(4)]
    MaterialRankFlags: CharacterRarityFlags
    # [Description("Material2")]
    # [PropertyOrder(5)]
    MaterialRankSecondFlags: CharacterRarityFlags
    # [Description("RankFlags")]
    # [PropertyOrder(3)]
    RankFlags: CharacterRarityFlags
    # [Description("ランクアップを完了すると適用されるランク")]
    # [PropertyOrder(6)]
    RankUpResultRarityFlags: CharacterRarityFlags
    # [Description("ランクアップ時の方法")]
    # [PropertyOrder(2)]
    UpType: RankUpType

# [Description("キャラクタープロフィール")]
# [MessagePackObject(True)]
@dataclass
class CharacterProfileMB(MasterBookBase):
    # [Description("誕生日")]
    # [PropertyOrder(4)]
    Birthday: int
    # [Description("血液型")]
    # [PropertyOrder(5)]
    BloodType: CharacterBloodType
    # [Description("CV(JP)キー")]
    # [PropertyOrder(10)]
    CharacterVoiceJPKey: str
    # [Description("CV(US)キー")]
    # [PropertyOrder(11)]
    CharacterVoiceUSKey: str
    # [Description("説明キー")]
    # [PropertyOrder(7)]
    DescriptionKey: str
    # [Description("専属武具の欠片ID")]
    # [PropertyOrder(6)]
    EquipmentCompositeId: int
    # [Description("新キャラ演出メッセージ2キー")]
    # [PropertyOrder(16)]
    GachaResultMessage2Key: str
    # [Description("身長")]
    # [PropertyOrder(2)]
    Height: int
    # [Description("ラメント(JP)キー")]
    # [PropertyOrder(12)]
    LamentJPKey: str
    # [Description("ラメント(US)キー")]
    # [PropertyOrder(13)]
    LamentUSKey: str
    # [Description("日本語キャラソン歌詞")]
    # [PropertyOrder(17)]
    LyricsJPKey: str
    # [Description("英語キャラソン歌詞")]
    # [PropertyOrder(18)]
    LyricsUSKey: str
    # [Description("動画配信サイトURL(JP)")]
    # [Nest(False, 0)]
    # [PropertyOrder(8)]
    MovieJpUrl: TranslatedText
    # [Description("動画配信サイトURL(JP)")]
    # [Nest(False, 0)]
    # [PropertyOrder(9)]
    MovieUsUrl: TranslatedText
    # [Description("歌手(JP)キー")]
    # [PropertyOrder(14)]
    VocalJPKey: str
    # [Description("歌手(US)キー")]
    # [PropertyOrder(15)]
    VocalUSKey: str
    # [Description("体重")]
    # [PropertyOrder(3)]
    Weight: int

# [Description("キャラクター潜在能力")]
# [MessagePackObject(True)]
@dataclass
class CharacterPotentialMB(MasterBookBase):
    # [Description("キャラクターレベル")]
    # [PropertyOrder(1)]
    CharacterLevel: int
    # [Description("キャラクターサブレベル")]
    # [PropertyOrder(2)]
    CharacterSubLevel: int
    # [Description("潜在能力合計値")]
    # [PropertyOrder(3)]
    TotalBaseParameter: int

# [Description("キャラクターレアリティ係数")]
# [MessagePackObject(True)]
@dataclass
class CharacterPotentialCoefficientMB(MasterBookBase):
    # [Description("初期レアリティ")]
    # [PropertyOrder(1)]
    InitialRarityFlags: CharacterRarityFlags
    # [Description("レアリティ係数")]
    # [Nest(False, 0)]
    # [PropertyOrder(3)]
    RarityCoefficientInfo: CharacterRarityCoefficientInfo
    # [Description("レアリティ")]
    # [PropertyOrder(2)]
    RarityFlags: CharacterRarityFlags

# [Description("キャラクター")]
# [MessagePackObject(True)]
@dataclass
class CharacterMB(MasterBookBase):
    # [Description("アクティブスキルIDのリスト")]
    # [PropertyOrder(11)]
    ActiveSkillIds: list[int]
    # [Description("潜在能力配分係数")]
    # [Nest(False, 0)]
    # [PropertyOrder(8)]
    BaseParameterCoefficient: BaseParameter
    # [Description("潜在能力配分合計係数")]
    # [PropertyOrder(9)]
    BaseParameterGrossCoefficient: int
    # [Description("二つ名タイプ")]
    # [PropertyOrder(3)]
    CharacterType: CharacterType
    # [Description("属性")]
    # [PropertyOrder(4)]
    ElementType: ElementType
    # [Description("初期バトルパラメータ")]
    # [Nest(False, 0)]
    # [PropertyOrder(7)]
    InitialBattleParameter: BattleParameter
    # [Description("アイテム時レアリティ")]
    # [PropertyOrder(15)]
    ItemRarityFlags: ItemRarityFlags
    # [Description("職業")]
    # [PropertyOrder(5)]
    JobFlags: JobFlags
    # [Description("名称(二つ名)キー")]
    # [PropertyOrder(2)]
    Name2Key: str
    # [Description("名称キー")]
    # [PropertyOrder(1)]
    NameKey: str
    # [Description("通常攻撃のID")]
    # [PropertyOrder(10)]
    NormalSkillId: int
    # [Description("パッシブスキルIDのリスト")]
    # [PropertyOrder(12)]
    PassiveSkillIds: list[int]
    # [Description("レアリティ")]
    # [PropertyOrder(6)]
    RarityFlags: CharacterRarityFlags
    # [Description("解放に必要な絆の数")]
    # [PropertyOrder(13)]
    RequireFragmentCount: int
    # [Description("新キャラの図鑑表示終了時間(JST)")]
    # [PropertyOrder(17)]
    EndTimeFixJST: str
    # [Description("新キャラの図鑑表示開始時間(JST)")]
    # [PropertyOrder(16)]
    StartTimeFixJST: str

# [Description("キャラク動画配信モード")]
# [MessagePackObject(True)]
@dataclass
class CharacterLiveModeMB(MasterBookBase):
    # [Description("終了時間(JP)")]
    # [PropertyOrder(4)]
    BgmEndTimeJP: float
    # [Description("終了時間(US)")]
    # [PropertyOrder(6)]
    BgmEndTimeUS: float
    # [Description("BGM(JP)")]
    # [PropertyOrder(1)]
    BgmPathJP: str
    # [Description("BGM(US)")]
    # [PropertyOrder(2)]
    BgmPathUS: str
    # [Description("開始時間(JP)")]
    # [PropertyOrder(3)]
    BgmStartTimeJP: float
    # [Description("開始時間(US)")]
    # [PropertyOrder(5)]
    BgmStartTimeUS: float

# [Description("キャラクターレベル")]
# [MessagePackObject(True)]
@dataclass
class CharacterLevelMB(MasterBookBase):
    # [Description("レベル")]
    # [PropertyOrder(1)]
    Level: int
    # [Description("レベルアップ必要アイテム")]
    # [Nest(False, 0)]
    # [PropertyOrder(2)]
    RequiredItemList: list[UserItem]

# [Description("キャラクター視聴可能ボイス")]
# [MessagePackObject(True)]
@dataclass
class CharacterDetailVoiceMB(MasterBookBase):
    # [Description("キャラクターId")]
    # [PropertyOrder(1)]
    CharacterId: int
    # [Description("キャラクターボイス分類")]
    # [PropertyOrder(4)]
    CharacterVoiceCategory: CharacterVoiceCategory
    # [Description("Path")]
    # [Nest(False, 0)]
    # [PropertyOrder(7)]
    Path: CharacterVoicePath
    # [Description("スクロールビューでの表示順（昇順）")]
    # [PropertyOrder(8)]
    SortOrder: int
    # [Description("ボイス再生時の字幕キー")]
    # [PropertyOrder(3)]
    SubtitleKey: str
    # [Description("解放条件")]
    # [PropertyOrder(5)]
    UnlockCondition: UnlockCharacterDetailVoiceType
    # [Description("ボタン表示用テキスト（解放済）キー")]
    # [PropertyOrder(2)]
    UnlockedVoiceButtonTextKey: str
    # [Description("クエストID")]
    # [PropertyOrder(6)]
    UnlockQuestId: int

# [Description("アルカナ解放報酬")]
# [MessagePackObject(True)]
@dataclass
class CharacterCollectionRewardMB(MasterBookBase):
    # [Description("構成キャラ数")]
    # [PropertyOrder(1)]
    CharacterCount: int
    # [Description("段階（アルカナレベル）")]
    # [PropertyOrder(2)]
    CollectionLevel: int
    # [Description("名称キー")]
    # [Nest(False, 0)]
    # [PropertyOrder(3)]
    RewardItems: list[UserItem]

# [Description("アルカナ")]
# [MessagePackObject(True)]
@dataclass
class CharacterCollectionMB(MasterBookBase):
    # [Description("名称キー")]
    # [PropertyOrder(1)]
    NameKey: str
    # [Description("開放に必要なキャラーIDリスト")]
    # [PropertyOrder(2)]
    RequiredCharacterIds: list[int]
    # [Description("新アルカナの終了時間(JST)")]
    # [PropertyOrder(4)]
    EndTimeFixJST: str
    # [Description("新アルカナの開始時間(JST)")]
    # [PropertyOrder(3)]
    StartTimeFixJST: str

# [Description("アルカナレベル")]
# [MessagePackObject(True)]
@dataclass
class CharacterCollectionLevelMB(MasterBookBase):
    # [Description("開放後適用されるベースパラメータ")]
    # [Nest(False, 0)]
    # [PropertyOrder(4)]
    BaseParameterChangeInfos: list[BaseParameterChangeInfo]
    # [Description("開放後適用されるバトルパラメータ")]
    # [Nest(False, 0)]
    # [PropertyOrder(5)]
    BattleParameterChangeInfos: list[BattleParameterChangeInfo]
    # [Description("キャラクターレアリティ増加")]
    # [PropertyOrder(6)]
    CharacterRarityBonus: int
    # [Description("アルカナレベル解放条件")]
    # [PropertyOrder(3)]
    CharacterRarityFlags: CharacterRarityFlags
    # [Description("アルカナMBのID")]
    # [PropertyOrder(1)]
    CollectionId: int
    # [Description("アルカナレベル")]
    # [PropertyOrder(2)]
    CollectionLevel: int

# [Description("キャラクターボックスサイズ")]
# [MessagePackObject(True)]
@dataclass
class CharacterBoxSizeMB(MasterBookBase):
    # [Description("倉庫所持上限")]
    # [PropertyOrder(2)]
    BoxSize: int
    # [Description("レベル")]
    # [PropertyOrder(1)]
    Lv: int
    # [Description("必要仮想通貨数")]
    # [PropertyOrder(3)]
    RequiredCurrency: int

# [Description("章")]
# [MessagePackObject(True)]
@dataclass
class ChapterMB(MasterBookBase):
    # [Description("名称キー")]
    # [PropertyOrder(2)]
    NameKey: str
    # [Description("国ID")]
    # [MasterBookId(typeof)]
    # [PropertyOrder(1)]
    StateId: int
    # [Description("テキストキー")]
    # [PropertyOrder(3)]
    TextKey: str
    # [Description("領地名")]
    # [PropertyOrder(4)]
    TerritoryNameKey: str

# [Description("アイテム変換情報")]
# [MessagePackObject(True)]
@dataclass
class ChangeItemMB(MasterBookBase):
    # [Description("変換されるアイテムリスト")]
    # [Nest(False, 0)]
    # [PropertyOrder(5)]
    ChangeItems: list[UserItem]
    # [Description("アイテム変換タイプ")]
    # [PropertyOrder(1)]
    ChangeItemType: ChangeItemType
    # [Description("アイテムID")]
    # [PropertyOrder(3)]
    ItemId: int
    # [Description("アイテム種別")]
    # [PropertyOrder(2)]
    ItemType: ItemType
    # [Description("変換に必要な数")]
    # [PropertyOrder(4)]
    NeedCount: int

# [Description("祈りの泉　イベント")]
# [MessagePackObject(True)]
@dataclass
class BountyQuestEventMB(MasterBookBase):
    # [Description("イベント説明")]
    # [PropertyOrder(2)]
    EventDescriptionKey: str
    # [Description("イベント名")]
    # [PropertyOrder(1)]
    EventNameKey: str
    # [Description("報酬量の増加率(%)")]
    # [PropertyOrder(5)]
    MultipleNumber: int
    # [Description("対象となるアイテムリスト")]
    # [Nest(False, 0)]
    # [PropertyOrder(7)]
    TargetItemList: list[BountyQuestEventTargetItemInfo]
    # [Description("対象となる祈りの泉クエストタイプ")]
    # [Nest(False, 0)]
    # [PropertyOrder(6)]
    TargetQuestTypeList: list[BountyQuestEventTargetQuestTypeInfo]
    # [Description("終了時刻")]
    # [PropertyOrder(4)]
    EndTime: str
    # [Description("開始時刻")]
    # [PropertyOrder(3)]
    StartTime: str

# [Description("ボスデータ")]
# [MessagePackObject(True)]
@dataclass
class BossBattleEnemyMB(MasterBookBase):
    # [Description("アクティブスキルIDのリスト")]
    # [PropertyOrder(12)]
    ActiveSkillIds: list[int]
    # [Description("ベースパラメータ")]
    # [Nest(True, 1)]
    # [PropertyOrder(9)]
    BaseParameter: BaseParameter
    # [Description("バトルパラメータ")]
    # [Nest(True, 1)]
    # [PropertyOrder(10)]
    BattleParameter: BattleParameter
    # [Description("戦闘力")]
    # [PropertyOrder(5)]
    BattlePower: int
    # [Description("レアリティ")]
    # [PropertyOrder(8)]
    CharacterRarityFlags: CharacterRarityFlags
    # [Description("属性")]
    # [PropertyOrder(7)]
    ElementType: ElementType
    # [Description("敵調整ID")]
    # [PropertyOrder(16)]
    EnemyAdjustId: int
    # [Description("敵キャラID")]
    # [PropertyOrder(14)]
    BattleEnemyCharacterId: int
    # [Description("敵武具ID")]
    # [PropertyOrder(15)]
    EnemyEquipmentId: int
    # [Description("敵のランク")]
    # [PropertyOrder(4)]
    EnemyRank: int
    # [Description("職業")]
    # [PropertyOrder(6)]
    JobFlags: JobFlags
    # [Description("名称キー")]
    # [PropertyOrder(3)]
    NameKey: str
    # [Description("通常攻撃として使ってくるスキルID")]
    # [PropertyOrder(11)]
    NormalSkillId: int
    # [Description("パッシブスキルIDのリスト")]
    # [PropertyOrder(13)]
    PassiveSkillIds: list[int]
    # [Description("ユニットアイコンID")]
    # [PropertyOrder(2)]
    UnitIconId: int
    # [Description("ユニットアイコンタイプ")]
    # [PropertyOrder(1)]
    UnitIconType: UnitIconType

# [Description("祈りの泉　ボードランク")]
# [MessagePackObject(True)]
@dataclass
class BoardRankMB(MasterBookBase):
    # [Description("必要条件リスト")]
    # [Nest(False, 0)]
    # [PropertyOrder(2)]
    BoardRankConditionInfos: list[BoardRankConditionInfo]
    # [Description("開放クエスト最大レベル")]
    # [PropertyOrder(3)]
    OpenBountyQuestMaxRarity: BountyQuestRarityFlags
    # [Description("開放クエスト最低レベル")]
    # [PropertyOrder(4)]
    OpenBountyQuestMinRarity: BountyQuestRarityFlags
    # [Description("クエスト抽選リスト詳細ID")]
    # [PropertyOrder(5)]
    QuestLotteryInfoListId: int
    # [Description("ランク")]
    # [PropertyOrder(1)]
    Rank: int

# [Description("バトルスキル演出設定")]
# [MessagePackObject(True)]
@dataclass
class BattleSkillNameSettingMB(MasterBookBase):
    # [Description("アクティブスキルID(ActiveSkillMB)")]
    # [PropertyOrder(1)]
    ActiveSkillId: int
    # [Description("改行位置設定 JP")]
    # [PropertyOrder(2)]
    NewLineIndexJP: int
    # [Description("改行位置設定 US")]
    # [PropertyOrder(3)]
    NewLineIndexUS: int
    # [Description("改行位置設定 KR")]
    # [PropertyOrder(2)]
    NewLineIndexKR: int
    # [Description("改行位置設定 TW")]
    # [PropertyOrder(3)]
    NewLineIndexTW: int

# [Description("バトルスキル演出設定")]
# [MessagePackObject(True)]
@dataclass
class BattleSkillCharacterSettingMB(MasterBookBase):
    # [Description("キャラID (CharacterMB)")]
    # [PropertyOrder(1)]
    CharacterId: int
    # [Description("文字背景色タイプ")]
    # [PropertyOrder(2)]
    CharacterColorType: CharacterColorType

# [Description("バトルスケジュール")]
# [MessagePackObject(True)]
@dataclass
class BattleScheduleMB(MasterBookBase):
    # [Description("バトルタイプ")]
    # [PropertyOrder(1)]
    BattleScheduleType: BattleScheduleType
    # [Description("最大クエストID")]
    # [PropertyOrder(2)]
    MaxQuestId: int
    # [Description("開始日時")]
    # [PropertyOrder(3)]
    StartTimeFixJST: str

# [Description("放置バトル敵データ")]
# [MessagePackObject(True)]
@dataclass
class AutoBattleEnemyMB(MasterBookBase):
    # [Description("アクティブスキルIDのリスト")]
    # [PropertyOrder(12)]
    ActiveSkillIds: list[int]
    # [Description("ベースパラメータ")]
    # [Nest(True, 1)]
    # [PropertyOrder(9)]
    BaseParameter: BaseParameter
    # [Description("敵キャラクターID")]
    # [PropertyOrder(16)]
    BattleEnemyCharacterId: int
    # [Description("バトルパラメータ")]
    # [Nest(True, 1)]
    # [PropertyOrder(10)]
    BattleParameter: BattleParameter
    # [Description("戦闘力")]
    # [PropertyOrder(5)]
    BattlePower: int
    # [Description("レアリティ")]
    # [PropertyOrder(8)]
    CharacterRarityFlags: CharacterRarityFlags
    # [Description("属性")]
    # [PropertyOrder(7)]
    ElementType: ElementType
    # [Description("敵調整ID")]
    # [PropertyOrder(18)]
    EnemyAdjustId: int
    # [Description("敵武具ID")]
    # [PropertyOrder(17)]
    EnemyEquipmentId: int
    # [Description("敵のランク")]
    # [PropertyOrder(4)]
    EnemyRank: int
    # [Description("職業")]
    # [PropertyOrder(6)]
    JobFlags: JobFlags
    # [Description("名称キー")]
    # [PropertyOrder(3)]
    NameKey: str
    # [Description("通常攻撃として使ってくるスキルID")]
    # [PropertyOrder(11)]
    NormalSkillId: int
    # [Description("パッシブスキルIDのリスト")]
    # [PropertyOrder(13)]
    PassiveSkillIds: list[int]
    # [Description("ドロップするキャラクター経験値")]
    # [PropertyOrder(14)]
    RewardCharacterExp: int
    # [Description("ドロップするプレイヤー経験値")]
    # [PropertyOrder(15)]
    RewardPlayerExp: int
    # [Description("ユニットアイコンID")]
    # [PropertyOrder(2)]
    UnitIconId: int
    # [Description("ユニットアイコンタイプ")]
    # [PropertyOrder(1)]
    UnitIconType: UnitIconType

# [Description("アプリバージョン")]
# [MessagePackObject(True)]
@dataclass
class AppVersionMB(MasterBookBase):
    # [Description("デバイス種別")]
    # [PropertyOrder(1)]
    DeviceType: DeviceType
    # [Description("アプリバージョン")]
    # [PropertyOrder(2)]
    AppVersion: str

# [Description("アクティブスキル")]
# [MessagePackObject(True)]
@dataclass
class ActiveSkillMB(MasterBookBase):
    # [Description("サブセットスキルリスト")]
    # [Nest(True, 1)]
    # [PropertyOrder(4)]
    ActiveSkillInfos: list[ActiveSkillInfo]
    # [Description("スキル名キー")]
    # [PropertyOrder(1)]
    NameKey: str
    # [Description("初期スキルクールタイム")]
    # [PropertyOrder(2)]
    SkillInitCoolTime: int
    # [Description("スキルMAXクールタイム")]
    # [PropertyOrder(3)]
    SkillMaxCoolTime: int
    # [Description("ルートスキルID")]
    # [PropertyOrder(5)]
    RootActiveSkillId: int

