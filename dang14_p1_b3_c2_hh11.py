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


def bt_dang14_p1_b3_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thiết lập các bộ dữ liệu để đảm bảo góc đẹp (30, 45, 60)
                # k_tex là độ dài SA theo a, val là giá trị số, ans là đáp án tương ứng
                data_options = [
                    {'sa_tex': 'a\\sqrt{3}', 'val': sqrt(3), 'ans': '60^\\circ'},
                    {'sa_tex': 'a', 'val': 1, 'ans': '45^\\circ'},
                    {'sa_tex': 'a\\frac{\\sqrt{3}}{3}', 'val': Rational(1, 3)*sqrt(3), 'ans': '30^\\circ'}
                ]

                selected = random.choice(data_options)
                sa_val_tex = selected['sa_tex']
                ket_qua = selected['ans']

                # Tạo danh sách các phương án nhiễu
                all_ans = ['30^\\circ', '45^\\circ', '60^\\circ', '90^\\circ']
                if ket_qua in all_ans:
                    all_ans.remove(ket_qua)

                random.shuffle(all_ans)
                da_s1 = '$' + all_ans[0] + '$'
                da_s2 = '$' + all_ans[1] + '$'
                da_s3 = '$' + all_ans[2] + '$'
                da_d = '\\True $' + ket_qua + '$'

                # Trộn các phương án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Vẽ hình bằng TikZ


                # Nội dung câu hỏi
                noidungcauhoi = ('''\\immini{Cho hình chóp $S.ABCD$ có đáy $ABCD$ cạnh $a$, $SA$ vuông góc với đáy và $SA = %s$. Góc giữa đường thẳng $SD$ và mặt phẳng $(ABCD)$ bằng}
                                 { \\begin{tikzpicture}[line cap=round,line join=round,>=stealth,x=1.0cm,y=1.0cm, scale=0.8, line width=1pt]
                                 \\coordinate (A) at (0,0);
                                 \\coordinate (B) at (-1.5,-1.5);
                                 \\coordinate (D) at (3,0);
                                 \\coordinate (C) at (1.5,-1.5);
                                 \\coordinate (S) at (0,3);
                                 \\draw [dashed] (S)--(A) (A)--(B) (A)--(D);
                                 \\draw (S)--(B)--(C)--(D)--(S) (S)--(C);
                                 \\node at (A) [left] {$A$};
                                 \\node at (B) [below left] {$B$};
                                 \\node at (C) [below right] {$C$};
                                 \\node at (D) [right] {$D$};
                                 \\node at (S) [above] {$S$};
                                 \\draw (2.7,0) arc (180:150:0.5);
                                 \\end{tikzpicture}} '''
                                 % (sa_val_tex))

                # Nội dung lời giải chi tiết
                loigiai = ('''Vì $SA \\perp (ABCD)$ nên $A$ là hình chiếu vuông góc của $S$ lên mặt phẳng $(ABCD)$.\\\\
                             Do đó, $AD$ là hình chiếu vuông góc của $SD$ lên mặt phẳng $(ABCD)$.\\\\
                             Suy ra góc giữa đường thẳng $SD$ và mặt phẳng $(ABCD)$ là góc giữa $SD$ và $AD$, hay là góc $\\widehat{SDA}$.\\\\
                             Trong tam giác $SDA$ vuông tại $A$, ta có:\\\\
                             $\\tan \\widehat{SDA} = \\frac{SA}{AD} = \\frac{%s}{a} = %s$.\\\\
                             Vậy $\\widehat{SDA} = %s$.'''
                           % (sa_val_tex, latex(selected['val']), ket_qua))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n' 
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

