# fsdet

neural network model for recognizing fires and smoke in production and storage facilities

## used technologies

- python
- yolo v8
- opencv2
- kaggle vm

> coded in neovim :-)

## screenshot

![showcase](./gitdocs/showcase.png)

## installation

```bash
git clone https://github.com/mishkafreddy2009/fsdet.git
cd fsdet
python -m venv .venv
source ./.venv/bin/activate
pip install -r requirements.txt
```
## usage

```bash
# for default configuration
python main.py

# if you have custom model
python main.py --model <model path>

# if you have custom video file
python main.py -v <video file path>

# if you have both
python main.py --model <model path> -v <video file path>
```

## todo
- [ ] train new main model (best96eps_2dt) to 200 epochs and see what it looks like;
- [ ] collect new selfmade dataset;
- [ ] markup new dataset;
- [ ] train to 100 epochs new model;
