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


def bt_dang5_p3_b1_c1_hh11(self):
    # Khai báo biến
    # Các bộ số (a, b) cho tỉ lệ SM = a/b SD đảm bảo kết quả là số thập phân gọn gàng
    variants = [(1, 3), (1, 4), (2, 3), (3, 7), (1, 9)]
    a, b = random.choice(variants)

    # Tính toán kết quả
    correct_val = round((2 * a) / (a + b), 1)
    kq_str = str(correct_val).replace('.', ',')

    # Tạo các đáp án gây nhiễu
    options = []
    for offset in [0.1, -0.1, 0.2, -0.2, 0.3, -0.3, 0.4]:
        val = round(correct_val + offset, 1)
        if val > 0:
            options.append(str(val).replace('.', ','))

    # Loại bỏ giá trị trùng với đáp án đúng và lấy 3 đáp án sai
    options = list(set(options) - {kq_str})
    distractors = random.sample(options, 3)

    # Định dạng các đáp án trắc nghiệm
    da = '$%s$' % kq_str
    das1 = '$%s$' % distractors[0]
    das2 = '$%s$' % distractors[1]
    das3 = '$%s$' % distractors[2]

    # Câu hỏi
    noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy là hình thang $ABCD$ với $AD // BC$ và $AD = 2BC$. Gọi $M$ là điểm trên cạnh $SD$ thỏa mãn $SM = \\frac{%s}{%s} SD$. Mặt phẳng $(ABM)$ cắt cạnh bên $SC$ tại điểm $N$. Tỉ số $\\frac{SN}{SC}$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).''' % (a, b))

    # Các đáp án
    da_d = ('\\True ' + str(da))
    da_s1 = str(das1)
    da_s2 = str(das2) 
    da_s3 = str(das3) 

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)

    # Nội dung lời giải
    loigiai = ('''\\begin{center}
    \\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,3);
    \\coordinate (D) at (6,3);
    \\coordinate (B) at (1.5,1);
    \\coordinate (C) at (4.5,1);
    \\coordinate (F) at (3,-1);
    \\coordinate (S) at (3,7);
    \\coordinate (M) at ($(S)!%s/%s!(D)$);
    \\coordinate (N) at ($(S)!%s/%s!(C)$);
    \\coordinate (E) at ($(M)!0.5!(D)$);
    \\draw[line width=1pt] (S)--(A) (S)--(B) (S)--(C) (S)--(D);
    \\draw[line width=1pt] (A)--(B) (B)--(F) (C)--(F) (C)--(D) (M)--(N);
    \\draw[line width=1pt, dashed] (A)--(D) (B)--(C) (A)--(M)  (B)--(N);
    \\draw[line width=1pt] (F)--(N) (M)--(E) (C)--(E);
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[left] {$B$};
    \\fill (C) circle (1pt) node[right] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (S) circle (1pt) node[above] {$S$};
    \\fill (F) circle (1pt) node[below] {$F$};
    \\fill (M) circle (1pt) node[right] {$M$};
    \\fill (N) circle (1pt) node[right] {$N$};
    \\fill (E) circle (1pt) node[right] {$E$};
    \\end{tikzpicture}
    \\end{center}
    Gọi $F$ là giao điểm của $AB$ và $CD$. Nối $F$ với $M$, $FM$ cắt $SC$ tại điểm $N$. Khi đó $N$ là giao điểm của $(ABM)$ và $SC$. \\\\
    Theo giả thiết, ta chứng minh được $C$ là trung điểm $DF$. \\\\
    Trong mặt phẳng $(SCD)$ kẻ $CE$ song song $NM$ ($E$ thuộc $SD$). Do $C$ là trung điểm $DF$ nên suy ra $E$ là trung điểm $MD$. Khi đó, ta có $MD = 2ED \\Rightarrow ED = ME = \\frac{1}{2}MD$. \\\\
    Ta có $SM = \\frac{%s}{%s} SD \\Rightarrow MD = \\frac{%s}{%s} SD$. \\\\
    Suy ra $ME = \\frac{1}{2} \\cdot \\frac{%s}{%s} SD = \\frac{%s}{%s} SD$. \\\\
    Do $MN // CE$ nên áp dụng định lý Thales trong tam giác $SCE$, ta có: $\\frac{SN}{SC} = \\frac{SM}{SE}$. \\\\
    Ta có $SE = SM + ME = \\frac{%s}{%s} SD + \\frac{%s}{%s} SD = \\frac{%s}{%s} SD$. \\\\
    Từ đó suy ra $\\frac{SN}{SC} = \\frac{\\frac{%s}{%s}}{\\frac{%s}{%s}} = \\frac{%s}{%s} = %s$.''' % (
        a, b, 2 * a, a + b,
        a, b, b - a, b,
        b - a, b, b - a, 2 * b,
        a, b, b - a, 2 * b, a + b, 2 * b,
        a, b, a + b, 2 * b, 2 * a, a + b, kq_str
    ))
    dapan='\\shortans[0]{$%s$}\n'%(kq_str)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
        '\\loigiai{\n'+str(loigiai)+'\n}\n'
        '\\end{ex}\n\\end{minipage} \n\n')
    return content      

