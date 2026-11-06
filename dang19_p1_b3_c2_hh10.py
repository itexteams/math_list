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


def bt_dang19_p1_b3_c2_hh10(self):
            # Khai báo biến
            # 1. Random đường trung tuyến: (Đỉnh, Trung điểm, Đỉnh đáy 1, Đỉnh đáy 2)
            medians_pool = [('A', 'M', 'B', 'C'), ('B', 'N', 'A', 'C'), ('C', 'P', 'A', 'B')]
            V, M, P1, P2 = random.choice(medians_pool)

            # 2. Ngân hàng các mối quan hệ vectơ trên đường trung tuyến
            # Cấu trúc: (Vectơ 1, Vectơ 2, Hệ số k đúng, Giải thích độ dài, Giải thích hướng)
            relations = [
                (f"\\overrightarrow{{{V}G}}", f"\\overrightarrow{{G{M}}}", "2", f"{V}G = 2G{M}", "cùng hướng"),
                (f"\\overrightarrow{{G{V}}}", f"\\overrightarrow{{G{M}}}", "-2", f"G{V} = 2G{M}", "ngược hướng"),
                (f"\\overrightarrow{{{V}G}}", f"\\overrightarrow{{{V}{M}}}", "\\frac{2}{3}", f"{V}G = \\frac{{2}}{{3}}{V}{M}", "cùng hướng"),
                (f"\\overrightarrow{{G{V}}}", f"\\overrightarrow{{{V}{M}}}", "-\\frac{2}{3}", f"G{V} = \\frac{{2}}{{3}}{V}{M}", "ngược hướng"),
                (f"\\overrightarrow{{G{M}}}", f"\\overrightarrow{{{V}{M}}}", "\\frac{1}{3}", f"G{M} = \\frac{{1}}{{3}}{V}{M}", "cùng hướng"),
                (f"\\overrightarrow{{{M}G}}", f"\\overrightarrow{{{V}{M}}}", "-\\frac{1}{3}", f"{M}G = \\frac{{1}}{{3}}{V}{M}", "ngược hướng"),
                (f"\\overrightarrow{{G{M}}}", f"\\overrightarrow{{{V}G}}", "\\frac{1}{2}", f"G{M} = \\frac{{1}}{{2}}{V}G", "cùng hướng"),
                (f"\\overrightarrow{{{M}G}}", f"\\overrightarrow{{{V}G}}", "-\\frac{1}{2}", f"{M}G = \\frac{{1}}{{2}}{V}G", "ngược hướng")
            ]

            # Bốc ngẫu nhiên 1 mối quan hệ làm đề bài
            vec1, vec2, correct_k, exp_len, exp_dir = random.choice(relations)

            # 3. Tạo đáp án nhiễu
            all_possible_k = ["2", "-2", "\\frac{2}{3}", "-\\frac{2}{3}", "\\frac{1}{3}", "-\\frac{1}{3}", "\\frac{1}{2}", "-\\frac{1}{2}"]
            all_possible_k.remove(correct_k) # Loại đáp án đúng ra khỏi list nhiễu
            distractors = random.sample(all_possible_k, 3)

            # 4. Nội dung câu hỏi
            noidungcauhoi = f"Cho tam giác $ABC$ với trung tuyến ${V}{M}$ và trọng tâm $G$. Tìm số thực $k$ thỏa mãn ${vec1} = k{vec2}$."

            # 5. Khởi tạo đáp án
            da_d = '\\True $' + correct_k + '$'
            da_s1 = '$' + distractors[0] + '$'
            da_s2 = '$' + distractors[1] + '$'
            da_s3 = '$' + distractors[2] + '$'

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # 6. Mã vẽ hình TikZ tự động bám theo biến
            tikz_code = f"""\\begin{{center}}
            \\begin{{tikzpicture}}[scale=0.7, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (A) at (2,3);
            \\coordinate (B) at (0,0);
            \\coordinate (C) at (5,0);
            \\path ({P1}) -- ({P2}) coordinate[midway] ({M});
            \\path ({V}) -- ({M}) coordinate[pos=0.6667] (G);
            \\draw[thick, blue!70!black] (A)--(B)--(C)--cycle;
            \\draw[thick, blue!70!black] ({V})--({M});
            \\fill[red] (A) circle (1.5pt) node[above, black] {{$A$}};
            \\fill[red] (B) circle (1.5pt) node[below left, black] {{$B$}};
            \\fill[red] (C) circle (1.5pt) node[below right, black] {{$C$}};
            \\fill[red] ({M}) circle (1.5pt) node[below, black] {{${M}$}};
            \\fill[red] (G) circle (1.5pt) node[above right, black] {{$G$}};
            \\end{{tikzpicture}}
            \\end{{center}}"""

            # 7. Nội dung lời giải (Đã chèn TikZ)
            loigiai = (f"{tikz_code}"
                       f"Vì ${exp_len}$, hai vectơ ${vec1}$ và ${vec2}$ {exp_dir} "
                       f"nên ${vec1} = {correct_k}{vec2}$. Vậy $k = {correct_k}$."
                       )

            # ================= XUẤT CÂU TRẮC NGHIỆM =================

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

