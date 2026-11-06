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


def bt_dang17_p1_b3_c2_hh10(self):
            # Khai báo biến
            # Khai báo các kịch bản: 
            # (Tên trung điểm, Cạnh, Vectơ 1, Vectơ 2 (bị nhân đôi), Vectơ tổng, Đáp án đúng, Các đáp án nhiễu, Tọa độ trung điểm TikZ, Nét vẽ phụ TikZ, Vị trí node)
            cases = [
                ('E', 'BC', '\\overrightarrow{BA}', '\\overrightarrow{EC}', '\\overrightarrow{BC}', '\\overrightarrow{BD}', 
                 ['\\overrightarrow{DB}', '\\overrightarrow{AC}', '\\overrightarrow{CA}'], '(2,0)', '(A)--(E)', 'below'),

                ('F', 'CD', '\\overrightarrow{CB}', '\\overrightarrow{FD}', '\\overrightarrow{CD}', '\\overrightarrow{CA}', 
                 ['\\overrightarrow{AC}', '\\overrightarrow{BD}', '\\overrightarrow{DB}'], '(4,1)', '(B)--(F)', 'right'),

                ('G', 'AD', '\\overrightarrow{DC}', '\\overrightarrow{GA}', '\\overrightarrow{DA}', '\\overrightarrow{DB}', 
                 ['\\overrightarrow{BD}', '\\overrightarrow{AC}', '\\overrightarrow{CA}'], '(2,2)', '(C)--(G)', 'above'),

                ('H', 'AB', '\\overrightarrow{AD}', '\\overrightarrow{HB}', '\\overrightarrow{AB}', '\\overrightarrow{AC}', 
                 ['\\overrightarrow{CA}', '\\overrightarrow{BD}', '\\overrightarrow{DB}'], '(0,1)', '(D)--(H)', 'left')
            ]

            # Bốc ngẫu nhiên 1 kịch bản
            chosen_case = random.choice(cases)
            mid_pt, side, vec1, vec_half, vec_full, ans, distractors, mid_coord, line_draw, mid_pos = chosen_case

            # Nội dung câu hỏi
            noidungcauhoi = f"Cho hình chữ nhật $ABCD$ có ${mid_pt}$ là trung điểm ${side}$. Khi đó ${vec1} + 2{vec_half}$ bằng"

            # Khởi tạo các đáp án
            da_d = f"\\True ${ans}$"
            da_s1 = f"${distractors[0]}$"
            da_s2 = f"${distractors[1]}$"
            da_s3 = f"${distractors[2]}$"

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Mã vẽ hình TikZ tự động bám theo biến
            tikz_code = f"""\\begin{{center}}
            \\begin{{tikzpicture}}[scale=0.7, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\draw[step=1cm,gray!30,very thin] (-0.5,-0.5) grid (4.5,2.5);
            \\coordinate (A) at (0,2);
            \\coordinate (B) at (0,0);
            \\coordinate (C) at (4,0);
            \\coordinate (D) at (4,2);
            \\coordinate ({mid_pt}) at {mid_coord};
            \\draw[thick, blue!70!black] (A)--(B)--(C)--(D)--cycle;
            \\draw[thick, blue!70!black] {line_draw};
            \\fill[red] (A) circle (1.5pt) node[above left, black] {{$A$}};
            \\fill[red] (B) circle (1.5pt) node[below left, black] {{$B$}};
            \\fill[red] (C) circle (1.5pt) node[below right, black] {{$C$}};
            \\fill[red] (D) circle (1.5pt) node[above right, black] {{$D$}};
            \\fill[red] ({mid_pt}) circle (1.5pt) node[{mid_pos}, black] {{${mid_pt}$}};
            \\end{{tikzpicture}}
            \\end{{center}}"""

            # Nội dung lời giải (Đã chèn TikZ)
            loigiai = (f"{tikz_code}"
                       f"Vì ${mid_pt}$ là trung điểm của ${side}$ nên $2{vec_half} = {vec_full}$.\\\\ "
                       f"Ta có: ${vec1} + 2{vec_half} = {vec1} + {vec_full} = {ans}$ (theo quy tắc hình bình hành)."
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

