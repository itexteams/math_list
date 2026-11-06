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


def bt_dang13_p3_b1_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Random hệ số k để tạo bài toán mới (k = 2 là bài toán gốc)
        k = random.choice([2, 3, 4])

        # Tính toán kết quả
        ans_val = sp.Rational(2 * k, k - 1)
        kqz=2*k/(k-1)
        number = Decimal(float(kqz))  # Số cần làm tròn
        kq_texz = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_tex=str(kq_texz).replace('.', ',')
        # Các đáp án trắc nghiệm
        du = ['$%s$' % (kq_tex)]
        da = random.choice(du)
        s = [
            '$%s$' % latex(ans_val + 1),
            '$%s$' % latex(ans_val + sp.Rational(1, 2)),
            '$%s$' % latex(ans_val - 1),
            '$%s$' % latex(ans_val + 2),
            '$%s$' % latex(sp.Rational(k - 1, 2 * k))
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Câu hỏi
        if k == 2:
            noidungcauhoi = ('Cho hình chóp $S.ABCD$ đáy $ABCD$ là hình bình hành. $M$, $N$ lần lượt là trung điểm của $AB$ và $SC$. $I$ là giao điểm của $AN$ và $(SBD)$. $J$ là giao điểm của $MN$ với $(SBD)$. Khi đó tỉ số $\\frac{IB}{IJ}$ bằng bao nhiêu?')
        else:
            noidungcauhoi = ('Cho hình chóp $S.ABCD$ đáy $ABCD$ là hình bình hành. $M$, $N$ là các điểm lần lượt trên $AB$ và $SC$ sao cho $AB = %s BM$ và $SC = %s SN$. $I$ là giao điểm của $AN$ và $(SBD)$. $J$ là giao điểm của $MN$ với $(SBD)$. Khi đó tỉ số $\\frac{IB}{IJ}$ bằng bao nhiêu?' % (k, k))

        # Hình vẽ TikZ (Hình ảnh không tô màu, nét 1pt theo đúng yêu cầu)
        tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (D) at (0,0);\n'
            '\\coordinate (C) at (5,0);\n'
            '\\coordinate (A) at (1.5,1.2);\n'
            '\\coordinate (B) at (6.5,1.2);\n'
            '\\coordinate (S) at (2.5,4.5);\n'
            '\\coordinate (O) at ($(A)!0.5!(C)$);\n'
            '\\coordinate (M) at ($(A)!0.5!(B)$);\n'
            '\\coordinate (N) at ($(S)!0.5!(C)$);\n'
            '\\coordinate (K) at ($(S)!0.5!(D)$);\n'
            '\\coordinate (I) at (intersection of A--N and S--O);\n'
            '\\coordinate (J) at (intersection of M--N and B--K);\n'
            '\\draw[line width=1pt] (S)--(D)--(C)--(B)--(S)--(C) (N)--(K);\n'
            '\\draw[line width=1pt, dashed] (S)--(A)--(D) (A)--(B) (A)--(C) (B)--(D) (S)--(O) (A)--(N) (M)--(N) (B)--(K) (A)--(K);\n'
            '\\fill (A) circle (1pt) node[left] {$A$};\n'
            '\\fill (B) circle (1pt) node[right] {$B$};\n'
            '\\fill (C) circle (1pt) node[right] {$C$};\n'
            '\\fill (D) circle (1pt) node[left] {$D$};\n'
            '\\fill (S) circle (1pt) node[above] {$S$};\n'
            '\\fill (O) circle (1pt) node[below] {$O$};\n'
            '\\fill (M) circle (1pt) node[below] {$M$};\n'
            '\\fill (N) circle (1pt) node[right] {$N$};\n'
            '\\fill (K) circle (1pt) node[left] {$K$};\n'
            '\\fill (I) circle (1pt) node[left] {$I$};\n'
            '\\fill (J) circle (1pt) node[right] {$J$};\n'
            '\\begin{scope}[shift={(7.5, 0)}]\n'
            '\\coordinate (B2) at (0,0);\n'
            '\\coordinate (M2) at (2,0);\n'
            '\\coordinate (A2) at (4,0);\n'
            '\\coordinate (N2) at (3,1);\n'
            '\\coordinate (K2) at (5,1);\n'
            '\\coordinate (J2) at (intersection of M2--N2 and B2--K2);\n'
            '\\coordinate (I2) at (intersection of A2--N2 and B2--K2);\n'
            '\\draw[line width=1pt] (B2)--(A2) (N2)--(K2) (B2)--(K2) (A2)--(N2) (M2)--(N2) (A2)--(K2);\n'
            '\\fill (B2) circle (1pt) node[left] {$B$};\n'
            '\\fill (M2) circle (1pt) node[below] {$M$};\n'
            '\\fill (A2) circle (1pt) node[right] {$A$};\n'
            '\\fill (N2) circle (1pt) node[above] {$N$};\n'
            '\\fill (K2) circle (1pt) node[right] {$K$};\n'
            '\\fill (J2) circle (1pt) node[below right] {$J$};\n'
            '\\fill (I2) circle (1pt) node[below right] {$I$};\n'
            '\\end{scope}\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        )

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải (Được tổng quát hóa để vừa bao hàm bài gốc khi k=2, vừa đáp ứng khi hệ số k thay đổi)
        if k == 2:
            loigiai = ('Gọi $O$ là trung điểm của $AC$ nên $O=AC \\cap BD$. Trong mặt phẳng $(SAC)$: $AN \\cap SO = I$ nên $I$ là giao điểm của $AN$ và $(SBD)$. Trong $(ABN)$ ta có $MN \\cap BI = J$ nên $J$ là giao điểm của $MN$ với $(SBD)$. Gọi $K$ là trung điểm của $SD$. Suy ra $NK // DC // AB$ và $BI \\cap SD = K$ hay $B$, $I$, $J$, $K$ thẳng hàng. Khi đó $NK // BM$ và $NK = MA = BM$ và tứ giác $AKMN$ là hình bình hành. Xét hai tam giác đồng dạng $\\Delta KJN$ và $\\Delta BJM$ có $\\frac{NK}{BM} = \\frac{MJ}{NJ} = \\frac{BJ}{JK} = 1$ suy ra $J$ là trung điểm của $MN$ và $J$ là trung điểm của $BK$ hay $BJ=JK$. Trong tam giác $\\Delta SAC$ có $I$ là trọng tâm của tam giác nên $\\frac{NI}{IA} = \\frac{1}{2}$. Do $AK // MN$ nên $\\frac{IJ}{IK} = \\frac{NI}{IA} = \\frac{1}{2} \\Rightarrow \\frac{IJ}{JK} = \\frac{1}{3} = \\frac{IJ}{BJ} \\Rightarrow \\frac{IJ}{BI} = \\frac{1}{4}$ hay $\\frac{IB}{IJ} = 4$.')
        else:
            loigiai = ('Gọi $O$ là trung điểm của $AC$ nên $O = AC \\cap BD$. Trong mặt phẳng $(SAC)$: $AN \\cap SO = I$ nên $I$ là giao điểm của $AN$ và $(SBD)$. Trong $(ABN)$ ta có $MN \\cap BI = J$ nên $J$ là giao điểm của $MN$ với $(SBD)$. \\\\ '
                       'Gọi $K$ thuộc $SD$ sao cho $SD = %s SK$. Suy ra $NK // DC // AB$ và $NK = \\frac{1}{%s} DC = \\frac{1}{%s} AB$. Lại có $BM = \\frac{1}{%s} AB$ nên $NK // BM$ và $NK = BM$. Suy ra tứ giác $MBNK$ là hình bình hành. Tứ giác này có hai đường chéo $MN$ và $BK$ cắt nhau tại $J$ nên $J$ là trung điểm của $BK$ hay $BJ = JK = \\frac{1}{2} BK$. \\\\ '
                       'Trong mặt phẳng $(SAC)$, áp dụng định lí Menelaus cho $\\Delta SOC$ với cát tuyến $A-I-N$ ta có: \\\\ '
                       '$\\frac{IS}{IO} \\cdot \\frac{AO}{AC} \\cdot \\frac{NC}{NS} = 1 \\Rightarrow \\frac{IS}{IO} \\cdot \\frac{1}{2} \\cdot (%s-1) = 1 \\Rightarrow \\frac{IS}{IO} = \\frac{2}{%s-1}$. \\\\ '
                       'Trong mặt phẳng $(SBD)$, kẻ $OE // BK$ ($E \\in SD$). Do $O$ là trung điểm $BD$ nên $OE$ là đường trung bình của $\\Delta DBK$, suy ra $E$ là trung điểm $DK$ và $OE = \\frac{1}{2} BK$. \\\\ '
                       'Ta có $KD = SD - SK = (%s-1)SK \\Rightarrow KE = \\frac{%s-1}{2} SK$. \\\\ '
                       'Do $IK // OE$, theo định lí Thales trong $\\Delta SOE$: \\\\ '
                       '$\\frac{IK}{OE} = \\frac{SK}{SE} = \\frac{SK}{SK + KE} = \\frac{1}{1 + \\frac{%s-1}{2}} = \\frac{2}{%s+1} \\Rightarrow IK = \\frac{2}{%s+1} OE = \\frac{1}{%s+1} BK$. \\\\ '
                       'Từ đó, ta có: $IJ = JK - IK = \\left( \\frac{1}{2} - \\frac{1}{%s+1} \\right) BK = \\frac{%s-1}{2(%s+1)} BK$; $IB = BK - IK = \\left( 1 - \\frac{1}{%s+1} \\right) BK = \\frac{%s}{%s+1} BK$. \\\\ '
                       'Vậy $\\frac{IB}{IJ} = \\frac{%s}{%s+1} : \\frac{%s-1}{2(%s+1)} = \\frac{%s}{%s}=%s$.' % (k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, 2*k, k-1,str(kq_tex)))
    dapan='\\shortans[0]{$%s$}\n'%(kq_tex)
    # Xuất câu trắc nghiệm
    content = (
        '\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
        '\\loigiai{\n' +str(tikz)+ str(loigiai) + '\n}\n'
        '\\end{ex}\n\\end{minipage} \n\n')
    return content  

