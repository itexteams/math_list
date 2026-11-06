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


def bt_dang15_p3_b2_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random độ dài hai cạnh góc vuông AB và BC sao cho CD dương và là số hữu tỉ
                while True:
                    ab_val = randint(4, 8)
                    bc_val = randint(2, ab_val - 1)


                    if ab_val > bc_val:
                        bd_rat = Rational(ab_val * (ab_val + bc_val), ab_val - bc_val)
                        cd_rat = bd_rat - bc_val
                        if cd_rat > 0:
                            break

                # Định dạng kết quả dạng phân số hoặc số nguyên
                if cd_rat.q == 1:
                    kq_str = str(cd_rat.p)
                else:
                    # Chuyển đổi dấu thập phân sang dấu phẩy nếu chia hết dạng thập phân, ngược lại giữ phân số tối giản
                    if cd_rat.q in [2, 4, 5, 10]:
                        kq_str = str(float(cd_rat)).replace('.', ',')
                    else:
                        kq_str = '\\frac{%s}{%s}' % (str(cd_rat.p), str(cd_rat.q))

                da = '$%s$' % kq_str

                # Tạo các phương án nhiễu không trùng đáp án đúng
                s = []
                for sai in [cd_rat + 1, cd_rat + 2, bd_rat, Rational(ab_val*bc_val, ab_val+bc_val), cd_rat * 2, cd_rat / 2]:
                    if sai != cd_rat and sai > 0:
                        if sai.q == 1:
                            val_sai = '$%s$' % str(sai.p)
                        elif sai.q in [2, 4, 5, 10]:
                            val_sai = '$%s$' % str(float(sai)).replace('.', ',')
                        else:
                            val_sai = '$%s$' % ('\\frac{%s}{%s}' % (str(sai.p), str(sai.q)))
                        if val_sai not in s:
                            s.append(val_sai)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Tính các phân số hiển thị trong lời giải
                tan_bac = Rational(bc_val, ab_val)
                tan_bad = Rational(ab_val + bc_val, ab_val - bc_val)

                # Chuỗi hiển thị phân số trong LaTeX
                str_tan_bac = '\\frac{%s}{%s}' % (str(bc_val), str(ab_val)) if tan_bac.q != 1 else str(tan_bac.p)
                str_tan_bad = '\\frac{%s}{%s}' % (str(tan_bad.p), str(tan_bad.q)) if tan_bad.q != 1 else str(tan_bad.p)
                str_bd = '\\frac{%s}{%s}' % (str(bd_rat.p), str(bd_rat.q)) if bd_rat.q != 1 else str(bd_rat.p)

                # Câu hỏi kèm hình vẽ TikZ độ dày nét 1pt
                noidungcauhoi = ('''Cho tam giác $ABC$ vuông tại $B$ và có hai cạnh góc vuông là $AB = %s, BC = %s$. Vẽ điểm $D$ nằm trên tia đối của tia $CB$ thỏa mãn $\\widehat{CAD} = 45^\\circ$ (Xem hình minh họa). Tính độ dài cạnh $CD$. \\\\
                                 \\begin{center} \\begin{tikzpicture}[scale=0.6, line width=1pt, >=stealth]
                                    \\coordinate (B) at (0,0);
                                    \\coordinate (A) at (0,4);
                                    \\coordinate (C) at (2,0);
                                    \\coordinate (D) at (7,0);
                                    \\draw (A) -- (B) -- (D) -- cycle;
                                    \\draw (A) -- (C);
                                    \\draw (0,0.5) -- (0.5,0.5) -- (0.5,0);
                                    \\node[left] at (B) {$B$};
                                    \\node[above left] at (A) {$A$};
                                    \\node[below] at (C) {$C$};
                                    \\node[below] at (D) {$D$};
                                    \\node[left] at (0,2) {$%s$};
                                    \\node[below] at (1,0) {$%s$};
                                    \\draw (0.4,3.2) arc (-60:-30:1);
                                    \\node at (1.2,2.8) {$45^\\circ$};
                                 \\end{tikzpicture} \\end{center}''' 
                                 % (latex(ab_val), latex(bc_val), latex(ab_val), latex(bc_val)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết rõ ràng từng bước
                loigiai = ('''Xét tam giác $ABC$ vuông tại $B$, ta có: $\\tan \\widehat{BAC} = \\frac{BC}{AB} = %s$. \\\\
                           Ta có $\\widehat{BAD} = \\widehat{BAC} + \\widehat{CAD} = \\widehat{BAC} + 45^\\circ$. \\\\
                           Suy ra: $\\tan \\widehat{BAD} = \\tan(\\widehat{BAC} + 45^\\circ) = \\frac{\\tan \\widehat{BAC} + \\tan 45^\\circ}{1 - \\tan \\widehat{BAC} \\cdot \\tan 45^\\circ} = \\frac{%s + 1}{1 - %s \\cdot 1} = %s$. \\\\
                           Mặt khác, trong tam giác $ABD$ vuông tại $B$, ta có: $\\tan \\widehat{BAD} = \\frac{BD}{AB} \\Rightarrow BD = AB \\cdot \\tan \\widehat{BAD} = %s \\cdot %s = %s$. \\\\
                           Độ dài cạnh $CD$ cần tìm là: $CD = BD - BC = %s - %s = %s$.'''
                           % (str_tan_bac, str_tan_bac, str_tan_bac, str_tan_bad,
                              latex(ab_val), str_tan_bad, str_bd,
                              str_bd, latex(bc_val), kq_str))
                dapan='\\shortans[0]{$%s$}\n'%(kq_str)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

