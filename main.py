from src.data.load_data import (
    load_dataset1_train,
    load_dataset2
)

def main():
    ds1_train = load_dataset1_train()
    ds2 = load_dataset2()

    print("Dataset 1 shape:", ds1_train.shape)
    print("Dataset 2 shape:", ds2.shape)


if __name__ == "__main__":
    main()
