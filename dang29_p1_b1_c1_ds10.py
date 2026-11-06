import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang29_p1_b1_c1_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Thiết lập các bộ dữ liệu ngẫu nhiên
        datasets = [
            (
                'hai tam giác bằng nhau',
                'diện tích hai tam giác đó bằng nhau',
                'hai tam giác có diện tích bằng nhau thì hai tam giác đó bằng nhau',
                'hai tam giác có diện tích không bằng nhau thì hai tam giác đó không bằng nhau',
                'hai tam giác bằng nhau thì hai tam giác đó có chu vi bằng nhau',
                'hai tam giác không bằng nhau thì diện tích hai tam giác đó không bằng nhau'
            ),
            (
                'một tứ giác là hình thoi',
                'hai đường chéo của nó vuông góc với nhau',
                'một tứ giác có hai đường chéo vuông góc với nhau thì tứ giác đó là hình thoi',
                'một tứ giác không là hình thoi thì hai đường chéo của nó không vuông góc với nhau',
                'một tứ giác là hình thoi thì nó có bốn cạnh bằng nhau',
                'một tứ giác có hai đường chéo không vuông góc với nhau thì tứ giác đó không là hình thoi'
            ),
            (
                'một tam giác là tam giác đều',
                'tam giác đó có ba góc bằng nhau',
                'một tam giác có ba góc bằng nhau thì tam giác đó là tam giác đều',
                'một tam giác không là tam giác đều thì tam giác đó không có ba góc bằng nhau',
                'một tam giác có ba cạnh bằng nhau thì tam giác đó có ba góc bằng nhau',
                'một tam giác không có ba góc bằng nhau thì tam giác đó không là tam giác đều'
            ),
            (
                'số tự nhiên n có chữ số tận cùng là 0',
                'số tự nhiên n chia hết cho 5',
                'số tự nhiên n chia hết cho 5 thì số tự nhiên n có chữ số tận cùng là 0',
                'số tự nhiên n không có chữ số tận cùng là 0 thì số tự nhiên n không chia hết cho 5',
                'số tự nhiên n chia hết cho 10 thì số tự nhiên n chia hết cho 5',
                'số tự nhiên n không chia hết cho 5 thì số tự nhiên n không có chữ số tận cùng là 0'
            )
        ]

        chosen_set = random.choice(datasets)

        P = chosen_set[0]
        Q = chosen_set[1]
        correct_ans = chosen_set[2]
        wrong_1 = chosen_set[3]
        wrong_2 = chosen_set[4]
        wrong_3 = chosen_set[5]

        noidungcauhoi = ('''Cho mệnh đề: "Nếu %s thì %s". Trong các mệnh đề sau đây, đâu là mệnh đề đảo của mệnh đề trên?'''
                            % (P, Q))

        da_d = ('\\True ' + '"Nếu ' + correct_ans + '"')
        da_s1 = ('"Nếu ' + wrong_1 + '"')
        da_s2 = ('"Nếu ' + wrong_2 + '"')
        da_s3 = ('"Nếu ' + wrong_3 + '"')

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        loigiai = ('''Mệnh đề đã cho có dạng "Nếu P thì Q" \\\\
                        Với: \\\\
                        P: "%s" \\\\
                        Q: "%s" \\\\
                        Mệnh đề đảo của mệnh đề trên có dạng "Nếu Q thì P", tức là: \\\\
                        "Nếu %s".\\\\
                        Do đó ta chọn phương án chứa mệnh đề này.'''
                    % (P, Q, correct_ans))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '{' + str(list_1[0]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('++','+').replace('--','+').replace('+-','-').replace('-+','-').replace('10x','10 x').replace('+0x','').replace('-0x','').replace('11x','11 x').replace('1x','x').replace('10y','10 y').replace('+0y','').replace('-0y','').replace('11y','11 y').replace('1y','y').replace('10t','10 t').replace('+0t','').replace('-0t','').replace('11t','11 t').replace('1t','t')
    return content

