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


def bt_dang14_p3_b2_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1', '2', '3']
    dang = random.choice(lisdang)

    if dang == '1':
        ratio_str = "\\frac{GM}{GN}"
        kq_val = 2.0
        final_line = "Từ (1) và (2), ta có $\\frac{GM}{GN} = 2,0$."
    elif dang == '2':
        ratio_str = "\\frac{GN}{GM}"
        kq_val = 0.5
        final_line = "Từ (1) và (2), ta có $\\frac{GM}{GN} = 2 \\Rightarrow \\frac{GN}{GM} = 0,5$."
    else:
        ratio_str = "\\frac{GM}{MN}"
        kq_val = 2 / 3
        final_line = "Từ (1) và (2), ta có $\\frac{GM}{GN} = 2 \\Rightarrow \\frac{GM}{MN} = \\frac{2}{3} \\approx 0,7$."

    # Xử lý kết quả đúng: Làm tròn 1 chữ số thập phân và đổi dấu chấm thành phẩy
    kq_dec = Decimal(float(kq_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
    s_str = str(kq_dec).replace('.', ',')

    du = ['$%s$' % s_str]
    da = du[0]

    # Tạo các phương án sai ngẫu nhiên (dành cho trường hợp bạn muốn dùng lại \choice)
    kq_f = float(kq_dec)
    s_list_raw = [
        kq_f + 0.1, 
        kq_f + 0.2, 
        abs(kq_f - 0.1) if kq_f - 0.1 > 0 else kq_f + 0.5, 
        kq_f + 1.0
    ]

    s_list = []
    for val in s_list_raw:
        val_dec = Decimal(str(val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        s_list.append('$%s$' % str(val_dec).replace('.', ','))

    # Loại bỏ các phương án trùng lặp với đáp án đúng
    s_list = list(set(s_list) - set(du))

    das1 = s_list[0]
    das2 = s_list[1]
    das3 = s_list[2]

    # Câu hỏi
    noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy là hình bình hành. Gọi $N$ là trung điểm của cạnh $SC$. Lấy điểm $M$ đối xứng với $B$ qua $A$. Gọi giao điểm $G$ của đường thẳng $MN$ với mặt phẳng $(SAD)$. Tỉ số $%s$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                     % (ratio_str))

    # Nội dung lời giải
    loigiai = ('''\\begin{center}
           \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (D) at (0,0);
            \\coordinate (C) at (4,0);
            \\coordinate (A) at (1,1.5);
            \\coordinate (B) at (5,1.5);
            \\coordinate (S) at (2,5);
            \\coordinate (M) at (-3,1.5);
            \\coordinate (N) at ($(S)!0.5!(C)$);
            \\coordinate (O) at ($(A)!0.5!(C)$);
            \\coordinate (K) at (intersection of M--O and A--D);
            \\coordinate (G) at (intersection of M--N and S--K);
            \\coordinate (I) at ($(A)!0.5!(B)$);
            \\draw[line width=1pt] (M)--(D)--(C)--(B)--(S)--(D) (S)--(C) (S)--(M) (M)--(A);
            \\draw[line width=1pt, dashed] (A)--(B) (A)--(C) (B)--(D) (M)--(O) (S)--(A) (S)--(K) (M)--(N) (O)--(I) (N)--(O);
            \\fill (S) circle (1pt) node[above] {$S$};
            \\fill (A) circle (1pt) node[above left] {$A$};
            \\fill (B) circle (1pt) node[right] {$B$};
            \\fill (C) circle (1pt) node[right] {$C$};
            \\fill (D) circle (1pt) node[below] {$D$};
            \\fill (M) circle (1pt) node[left] {$M$};
            \\fill (N) circle (1pt) node[right] {$N$};
            \\fill (G) circle (1pt) node[above left] {$G$};
            \\fill (K) circle (1pt) node[below left] {$K$};
            \\fill (O) circle (1pt) node[below] {$O$};
            \\fill (I) circle (1pt) node[above] {$I$};
           \\end{tikzpicture}
           \\end{center}
           Gọi giao điểm của $AC$ và $BD$ là $O$ và kẻ $OM$ cắt $AD$ tại $K$. Vì $O$ là trung điểm $AC$, $N$ là trung điểm $SC$ nên $ON // SA$ (tính chất đường trung bình). Vậy hai mặt phẳng $(MON)$ và $(SAD)$ cắt nhau tại giao tuyến $GK$ song song với $NO$. Áp dụng định lí Talet cho $GK // ON$, ta có:\\\\
           $\\frac{GM}{GN} = \\frac{KM}{KO}$ (1)\\\\
           Gọi $I$ là trung điểm của $AB$, vì $O$ là trung điểm của $BD$ nên theo tính chất đường trung bình, $OI // AD$, vậy theo định lí Talet:\\\\
           $\\frac{KM}{KO} = \\frac{AM}{AI} = \\frac{AB}{AI} = 2$. (2)\\\\
           %s''' % (final_line))

    dapan = '\\shortans[0]{$%s$}\n' % (s_str)

    # Xuất câu hỏi (Sử dụng format shortans theo mẫu cuối cùng của bạn cung cấp)
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n' + dapan +
        '\\loigiai{\n'+str(loigiai)+'\n}\n'
        '\\end{ex}\n\\end{minipage} \n\n')
    return content 

