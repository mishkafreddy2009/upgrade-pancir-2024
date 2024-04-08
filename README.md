# fsdet

neural network model for recognizing fires and smoke in production and storage facilities

**status** in early development...

![showcase](./gitdocs/showcase.png)

## used technologies

- python
- yolo v8
- opencv2

- powered by neovim

## installation

```bash
git clone https://github.com/mishkafreddy2009/fsdet.git
cd fsdet
# create envoriment
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
