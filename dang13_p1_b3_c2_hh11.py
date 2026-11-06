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


def bt_dang13_p1_b3_c2_hh11(self):
            # Khai báo biến
            # Danh sách các bộ đỉnh để random (Đỉnh chóp, Chân đường cao, Điểm 1 đáy, Điểm 2 đáy)
            list_labels = [
                ('S', 'A', 'B', 'C'),
                ('S', 'H', 'M', 'N'),
                ('S', 'K', 'P', 'Q'),
                ('S', 'A', 'M', 'N'),
                ('S', 'H', 'B', 'C')
            ]

            # Chọn ngẫu nhiên một bộ nhãn
            v_S, v_A, v_B, v_C = random.choice(list_labels)

            # Nội dung hình vẽ TikZ
            hinh_ve = (
                '\\begin{tikzpicture}[line cap=round, line join=round, line width=1pt, scale=1]\n'
                '  \\coordinate (A) at (0,0);\n'
                '  \\coordinate (B) at (1.2,-1.2);\n'
                '  \\coordinate (C) at (3.5,0);\n'
                '  \\coordinate (S) at (0,3);\n'
                '  \\draw [dashed] (A)--(C) ;\n'
                '  \\draw (S)--(A) (A)--(B);\n'
                '  \\draw (S)--(B)--(C)--(S);\n'
                '  \\tkzMarkRightAngle[size=0.3](S,A,B)\n'
                '  \\tkzMarkRightAngle[size=0.3](S,A,C)\n'
                '  \\draw (A) node[left]{$' + v_A + '$};\n'
                '  \\draw (B) node[below]{$' + v_B + '$};\n'
                '  \\draw (C) node[right]{$' + v_C + '$};\n'
                '  \\draw (S) node[above]{$' + v_S + '$};\n'
                '\\end{tikzpicture}\n'
            )

            # Nội dung câu hỏi
            noidungcauhoi = (
                '\\immini{Cho hình chóp $' + v_S + '.' + v_A + v_B + v_C + '$ có cạnh $' + v_S + v_A + '$ vuông góc với đáy. '
                'Góc giữa đường thẳng $' + v_S + v_B + '$ và mặt phẳng đáy là góc giữa hai đường thẳng nào dưới đây?}'
                '{'+ hinh_ve+'}'
            )

            # Đáp án đúng và các đáp án sai
            da_d = '\\True $' + v_S + v_B + '$ và $' + v_A + v_B + '$'
            da_s1 = '$' + v_S + v_B + '$ và $' + v_S + v_C + '$'
            da_s2 = '$' + v_S + v_A + '$ và $' + v_S + v_B + '$'
            da_s3 = '$' + v_S + v_B + '$ và $' + v_B + v_C + '$'

            # Trộn đáp án
            list_ans = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # Lời giải chi tiết
            loigiai = (
                'Ta có: Hình chiếu của $' + v_S + v_B + '$ trên mặt phẳng $(' + v_A + v_B + v_C + ')$ là $' + v_A + v_B + '$ '
                'nên góc giữa đường thẳng $' + v_S + v_B + '$ và mặt phẳng đáy là góc giữa hai đường thẳng $' + v_S + v_B + '$ và $' + v_A + v_B + '$.'
            )

            # Xuất nội dung theo cấu trúc mẫu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_ans[0]) + '}\n'
                '{' + str(list_ans[1]) + '}\n'
                '{' + str(list_ans[2]) + '}\n'
                '{' + str(list_ans[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content

