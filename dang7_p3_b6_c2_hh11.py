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


def bt_dang7_p3_b6_c2_hh11(self):
            # Khai báo biến
            # 1. Khai báo biến ngẫu nhiên
            val_a = randint(2, 5) 
            list_k = [2, 3, 5, 6]
            k = random.choice(list_k)

            # 2. Tính toán giá trị số thực
            # Chiều cao h = a * sqrt(k)
            h_val = val_a * (k**0.5)
            # Diện tích đáy S = a^2
            s_day = val_a**2
            # Thể tích V = (1/3) * S * h
            v_exact = (1/3) * s_day * h_val

            # 3. Làm tròn đến hàng phần chục (1 chữ số thập phân)
            v_rounded = round(v_exact, 1)

            # Định dạng hiển thị SA cho câu hỏi (vẫn giữ căn thức cho đẹp)
            sa_latex = latex(val_a * sqrt(k))

            # 4. Tạo đáp án đúng và các đáp án sai
            da_dung_str = f'$V \\approx {v_rounded}$'

            # Tạo các đáp án sai bằng cách làm tròn các giá trị khác
            # Đảm bảo các đáp án sai không trùng với đáp án đúng
            answers_set = {da_dung_str}
            while len(answers_set) < 4:
                # Tạo sai số ngẫu nhiên hoặc công thức sai (VD: quên chia 3, hoặc chia 2)
                sai_so = random.choice([v_exact * 3, v_exact / 2, v_exact + randint(5, 15)])
                s_str = f'$V \\approx {round(sai_so, 1)}$'
                answers_set.add(s_str)

            # 5. Câu hỏi
            noidungcauhoi = ('''Cho hình chóp tứ giác $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh $%s$, cạnh bên $SA$ vuông góc với mặt phẳng đáy và $SA = %s$. Thể tích $V$ của khối chóp $S.ABCD$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                             % (latex(val_a), sa_latex))

            # Xáo trộn đáp án
            list_ans = list(answers_set)
            # Đánh dấu đáp án đúng cho TeX (giả sử dùng gói lệnh có \True)
            list_ans = [('\\True ' + x if x == da_dung_str else x) for x in list_ans]
            random.shuffle(list_ans)

            da_s1, da_s2, da_s3, da_s4 = list_ans[0], list_ans[1], list_ans[2], list_ans[3]

            # 6. Nội dung lời giải
            hinh_ve = ('''\\begin{center}
            \\begin{tikzpicture}[line width=1pt, scale=0.8]
                \\coordinate (A) at (0,3);
                \\coordinate (B) at (4,3);
                \\coordinate (C) at (5,1);
                \\coordinate (D) at (1,1);
                \\coordinate (S) at (0,6.5);
                \\draw [dashed]  (A)--(B) ;
                \\draw (S)--(A) (S)--(B) (S)--(C) (S)--(D) (B)--(C) (C)--(D) (A)--(D);
                \\node at (S) [above] {$S$};
                \\node at (A) [left] {$A$};
                \\node at (B) [right] {$B$};
                \\node at (C) [right] {$C$};
                \\node at (D) [left] {$D$};
            \\end{tikzpicture}
            \\end{center}''')

            loigiai = ('''Ta có $SA \\perp \\left( ABCD \\right) \\Rightarrow SA$ là đường cao của hình chóp.\\\\
                         Diện tích đáy hình vuông $ABCD$ là: $S_{ABCD} = %s^2 = %s$.\\\\
                         Thể tích khối chóp $S.ABCD$ là: \\\\
                         $V = \\frac{1}{3} \\cdot SA \\cdot S_{ABCD} = \\frac{1}{3} \\cdot %s \\cdot %s \\approx %s$.'''
                       % (latex(val_a), latex(s_day), sa_latex, latex(s_day), v_rounded))
            dapan='\\shortans[0]{$%s$}\n'%(str(v_rounded).replace('.', ','))
            # 7. Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +str(dapan)+
                       '\\loigiai{\n' + hinh_ve + '\n' + str(loigiai) + '\n}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

