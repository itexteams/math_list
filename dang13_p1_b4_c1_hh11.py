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


def bt_dang13_p1_b4_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':

        # Các đáp án trắc nghiệm (không có dấu chấm ở cuối, thay || bằng //)
        da_d = ('\\True $MN // (ABCD)$')
        da_s1 = '$MN // (SAB)$'
        da_s2 = '$MN // (SAD)$'
        da_s3 = '$MN // (SCD)$'

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung câu hỏi
        noidungcauhoi = ('''%s''' % ('Cho hình chóp tứ giác $S.ABCD$. Gọi $M$ và $N$ lần lượt là trung điểm của $SA$ và $SC$. Khẳng định nào sau đây là đúng?'))

        # Hình vẽ TikZ chuẩn 100% như ảnh, nét vẽ 1pt, điểm 1pt, màu black, đã bỏ các gạch chéo ký hiệu hai đoạn bằng nhau
        hinhve = ('''\\begin{center}
            \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (S) at (2.5,4.5);
            \\coordinate (A) at (1.0,1.5);
            \\coordinate (D) at (1.7,-0.2);
            \\coordinate (C) at (4.4,0.3);
            \\coordinate (B) at (5.2,1.5);
            \\coordinate (M) at ($(S)!0.5!(A)$);
            \\coordinate (N) at ($(S)!0.5!(C)$);
            \\draw[line width=1pt] (S)--(A)--(D)--(C)--(B)--(S)--(D) (S)--(C);
            \\draw[line width=1pt, dashed] (A)--(B) (A)--(C) (M)--(N);
            \\fill (S) circle (1pt) node[above] {$S$};
            \\fill (A) circle (1pt) node[left] {$A$};
            \\fill (D) circle (1pt) node[below left] {$D$};
            \\fill (C) circle (1pt) node[right] {$C$};
            \\fill (B) circle (1pt) node[above right] {$B$};
            \\fill (M) circle (1pt) node[above left] {$M$};
            \\fill (N) circle (1pt) node[right] {$N$};
            \\end{tikzpicture}
            \\end{center}''')

        # Nội dung lời giải (trình bày chi tiết từng bước như ảnh, thay || bằng //)
        loigiai = ('''%s
    Vì $MN$ là đường trung bình của tam giác $SAC \\Rightarrow MN // AC$.\\\\
    Mặt khác $AC \\subset (ABCD) \\Rightarrow MN // (ABCD)$.'''
                   % (hinhve))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n\\choice \n' '{'+str(list_1[0])+'}\n' '{'+str(list_1[1])+'}\n' '{'+str(list_1[2])+'}\n' '{'+str(list_1[3])+'}\n' '\\loigiai{\n'+str(loigiai)+'\n}\n' '\\end{ex}\n \\end{minipage} \n\n')
    return content

