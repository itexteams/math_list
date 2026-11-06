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


def bt_dang26_p1_b3_c1_hh11(self):
    # Khai báo danh sách dạng bài
    lisdang = ['1', '2']
    dang = random.choice(lisdang)

    if dang == '1':
        # Dạng 1: Giữ nguyên như hình mẫu gốc
        # Tứ diện ABCD, G là trọng tâm tam giác ABD, M trên BC sao cho BM = 2MC
        # Đường thẳng MG song song với mặt phẳng (ACD)

        # Đáp án đúng
        da = '$(ACD)$'

        # Tập hợp các phương án gây nhiễu từ các mặt khác của tứ diện hoặc mặt phẳng qua điểm
        cac_mat = ['$(BCD)$', '$(ABD)$', '$(ABC)$', '$(ABM)$', '$(BCN)$', '$(DMN)$']
        s = [c for c in cac_mat if c != da]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Câu hỏi
        noidungcauhoi = ('''Cho tứ diện $ABCD$, $G$ là trọng tâm $\\Delta ABD$ và $M$ là điểm trên cạnh $BC$ sao cho $BM = 2MC$. Đường thẳng $MG$ song song với mặt phẳng nào sau đây?''')

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào danh sách và xáo trộn
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải với hình vẽ TikZ 100% như hình cung cấp
        loigiai = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (B) at (0,0);
    \\coordinate (C) at (2.2,-1.5);
    \\coordinate (A) at (4.5,0);
    \\coordinate (D) at (2.9,2.8);
    \\coordinate (N) at ($(A)!0.5!(D)$);
    \\coordinate (G) at ($(B)!0.66667!(N)$);
    \\coordinate (M) at ($(B)!0.66667!(C)$);
    \\draw[line width=1pt] (B)--(C)--(A)--(D)--cycle;
    \\draw[line width=1pt] (D)--(C) (C)--(N);
    \\draw[line width=1pt, dashed] (B)--(A) (B)--(N) (M)--(G);
    \\fill (B) circle (1pt) node[left] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (A) circle (1pt) node[below right] {$A$};
    \\fill (D) circle (1pt) node[above] {$D$};
    \\fill (N) circle (1pt) node[right] {$N$};
    \\fill (G) circle (1pt) node[above left] {$G$};
    \\fill (M) circle (1pt) node[below left] {$M$};
    \\end{tikzpicture}
    \\end{center}
    Gọi $N$ là trung điểm của $AD$. Do $G$ là trọng tâm của tam giác $ABD$ nên $\\frac{GB}{GN} = 2$.\\\\
    Xét trong tam giác $BCN$, ta có $\\frac{GB}{GN} = \\frac{MB}{MC} = 2$.\\\\
    Do đó $MG // CN$. Mà $CN \\subset (ACD)$ và $MG \\not\\subset (ACD)$.\\\\
    Vậy $MG // (ACD)$.''')

    elif dang == '2':
        # Dạng 2: Biến thể đảo vai trò điểm: M thuộc BD sao cho BM = 2MD
        # Đường thẳng MG // (ACD) (với N là trung điểm AB) hoặc tương đương
        # Ở đây: M trên cạnh CD sao cho CM = 2MD, G là trọng tâm tam giác BCD => MG // (ABD)

        da = '$(ABD)$'

        cac_mat = ['$(BCD)$', '$(ACD)$', '$(ABC)$', '$(BCM)$', '$(ABM)$', '$(DMN)$']
        s = [c for c in cac_mat if c != da]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        noidungcauhoi = ('''Cho tứ diện $ABCD$, $G$ là trọng tâm $\\Delta BCD$ và $M$ là điểm trên cạnh $AC$ sao cho $AM = 2MC$. Đường thẳng $MG$ song song với mặt phẳng nào sau đây?''')

        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        loigiai = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (B) at (0,0);
    \\coordinate (C) at (2.2,-1.5);
    \\coordinate (A) at (4.5,0);
    \\coordinate (D) at (2.9,2.8);
    \\coordinate (N) at ($(A)!0.5!(D)$);
    \\coordinate (G) at ($(B)!0.66667!(N)$);
    \\coordinate (M) at ($(B)!0.66667!(C)$);
    \\draw[line width=1pt] (B)--(C)--(A)--(D)--cycle;
    \\draw[line width=1pt] (D)--(C) (C)--(N);
    \\draw[line width=1pt, dashed] (B)--(A) (B)--(N) (M)--(G);
    \\fill (B) circle (1pt) node[left] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (A) circle (1pt) node[below right] {$A$};
    \\fill (D) circle (1pt) node[above] {$D$};
    \\fill (N) circle (1pt) node[right] {$N$};
    \\fill (G) circle (1pt) node[above left] {$G$};
    \\fill (M) circle (1pt) node[below left] {$M$};
    \\end{tikzpicture}
    \\end{center}
    Gọi $P$ là trung điểm của $BD$. Do $G$ là trọng tâm của tam giác $BCD$ nên $\\frac{CG}{CP} = \\frac{2}{3}$ hay $\\frac{GC}{GP} = 2$.\\\\
    Xét trong tam giác $ACP$, ta có $\\frac{MA}{MC} = \\frac{GC}{GP} = 2$.\\\\
    Do đó $MG // AP$. Mà $AP \\subset (ABD)$ và $MG \\not\\subset (ABD)$.\\\\
    Vậy $MG // (ABD)$.''')

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choice \n'
               '{' + str(list_1[1]) + '}\n'
               '{' + str(list_1[2]) + '}\n'
               '{' + str(list_1[3]) + '}\n'
               '{' + str(list_1[0]) + '}\n'
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content

