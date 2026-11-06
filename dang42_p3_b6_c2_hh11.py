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


def bt_dang42_p3_b6_c2_hh11(self):
            # Khai báo biến
            # Random hệ số k (khoảng cách là số thực)
            k = random.randint(1, 5) 
            dist = float(k)

            # Các thông số tính toán (sử dụng float để ra số thập phân)
            # Góc giữa (SBC) và (ABC) là 30 độ
            # AI = dist / sin(30) = 2 * dist
            ai_val = 2 * dist

            # SA = AI * tan(30)
            sa_val = ai_val * math.sqrt(3) / 3

            # Cạnh đáy x: AI = x * sqrt(3)/2 => x = 2*AI / sqrt(3)
            x_val = 2 * ai_val / math.sqrt(3)

            # Diện tích đáy ABC = x^2 * sqrt(3) / 4
            s_abc = (x_val**2 * math.sqrt(3)) / 4

            # Thể tích V = 1/3 * S_abc * SA
            v_val = (1/3) * s_abc * sa_val

            # Làm tròn kết quả cuối cùng đến hàng phần chục
            v_final = round(v_val, 1)

            # Định dạng các bước trung gian để hiển thị lời giải (làm tròn 2 chữ số cho đẹp)
            dist_str = str(int(dist)) if dist.is_integer() else str(round(dist, 2))
            ai_str = str(round(ai_val, 2))
            sa_str = str(round(sa_val, 2))
            x_str = str(round(x_val, 2))
            s_abc_str = str(round(s_abc, 2))
            v_str = str(v_final)

            # B4- Điều chỉnh các phương án sai
            da_dung = f'${v_str}$'

            # Tạo các đáp án nhiễu (số thập phân ngẫu nhiên quanh đáp án đúng)
            ds_sai = set()
            while len(ds_sai) < 3:
                sai = round(v_final * random.uniform(0.5, 2.0), 1)
                if sai != v_final:
                    ds_sai.add(f'${sai}$')

            # Trộn đáp án
            list_da = ['\\True ' + da_dung] + [item for item in ds_sai]
            random.shuffle(list_da)

            # B2- Viết lại nội dung câu hỏi và lời giải
            noidungcauhoi = ('''Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác đều, $SA \\perp \\left( ABC \\right)$. Mặt phẳng $\\left( SBC \\right)$ cách $A$ một khoảng bằng $%s$ và hợp với mặt phẳng $\\left( ABC \\right)$ góc $30^\\circ$. Thể tích của khối chóp $S.ABC$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                             % dist_str)

            # Vẽ hình bằng TikZ
            tikz_code = ('''\\begin{center} \\begin{tikzpicture}[line cap=round,line join=round,>=stealth,x=1.0cm,y=1.0cm, scale=0.8, line width=1pt]
            \\coordinate (A) at (0,0);
            \\coordinate (S) at (0,4);
            \\coordinate (B) at (1.5,-1.5);
            \\coordinate (C) at (5,0.5);
            \\coordinate (I) at ($(B)!0.5!(C)$);
            \\coordinate (H) at ($(S)!0.65!(I)$);
            \\draw [dashed] (A)--(C) (A)--(I) (A)--(H);
            \\draw (S)--(A)--(B)--(S)--(C)--(B) (S)--(I);
            \\tkzMarkRightAngle(S,A,I)
            \\tkzMarkRightAngle(A,H,I)
            \\tkzMarkRightAngle(A,I,B)
            \\draw (A) node[left]{$A$} (S) node[above]{$S$} (B) node[below]{$B$} (C) node[right]{$C$} (I) node[below right]{$I$} (H) node[above right]{$H$};
            \\tkzMarkAngle[size=0.7](S,I,A)
            \\node at ($(I)+(-0.9,0.4)$){$30^\\circ$};
            \\end{tikzpicture} \\end{center}''')

            loigiai = ('''%s
            Gọi $I$ là trung điểm của $BC$ suy ra góc giữa mp$\\left( SBC \\right)$ và mp$\\left( ABC \\right)$ là $\\widehat{SIA}=30^\\circ$. \\\\
            $H$ là hình chiếu vuông góc của $A$ trên $SI$ suy ra $d\\left( A, \\left( SBC \\right) \\right) = AH = %s$. \\\\
            Xét tam giác $AHI$ vuông tại $H$ suy ra $AI = \\frac{AH}{\\sin 30^\\circ} = %s$. \\\\
            Giả sử tam giác đều $ABC$ có cạnh bằng $x$, mà $AI$ là đường cao suy ra $%s = x \\cdot \\frac{\\sqrt{3}}{2} \\Rightarrow x \\approx %s$. \\\\
            Diện tích tam giác đều $ABC$ là $S_{ABC} = \\frac{x^2 \\sqrt{3}}{4} \\approx %s$. \\\\
            Xét tam giác $SAI$ vuông tại $A$ suy ra $SA = AI \\cdot \\tan 30^\\circ \\approx %s$. \\\\
            Vậy $V_{S.ABC} = \\frac{1}{3} \\cdot S_{ABC} \\cdot SA \\approx \\frac{1}{3} \\cdot %s \\cdot %s \\approx %s$.'''
                       % (tikz_code, dist_str, ai_str, ai_str, x_str, s_abc_str, sa_str, s_abc_str, sa_str, v_str))

            dapan = '\\shortans[0]{$%s$}\n' % (str(v_str).replace('.',','))
            # Xuất nội dung theo cấu trúc mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

