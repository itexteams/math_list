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


def bt_dang19_p3_b3_c2_hh11(self):
            # Khai báo biến
            # Chọn các góc đẹp: 30, 45, 60
            list_goc = [30, 45, 60]
            goc_chon = random.choice(list_goc)

            # Thiết lập SA dựa trên góc đã chọn
            # tan(goc) = SA / AC => SA = AC * tan(goc) = a*sqrt(2) * tan(goc)
            if goc_chon == 30:
                sa_latex = "\\frac{a\\sqrt{6}}{3}"
                sa_val = "a\\sqrt{6}/3"
            elif goc_chon == 45:
                sa_latex = "a\\sqrt{2}"
                sa_val = "a\\sqrt{2}"
            else: # 60 độ
                sa_latex = "a\\sqrt{6}"
                sa_val = "a\\sqrt{6}"

            # Đáp án đúng
            da_dung = "$%s^\\circ$" % goc_chon

            # Tạo danh sách các phương án sai (không trùng đáp án đúng)
            cac_goc_khac = [15, 30, 45, 60, 75]
            if goc_chon in cac_goc_khac:
                cac_goc_khac.remove(goc_chon)
            random.shuffle(cac_goc_khac)

            s = ["$%s^\\circ$" % cac_goc_khac[0],
                 "$%s^\\circ$" % cac_goc_khac[1],
                 "$%s^\\circ$" % cac_goc_khac[2]]

            # Gán biến cho các đáp án
            da_s1 = s[0]
            da_s2 = s[1]
            da_s3 = s[2]

            # Trộn các đáp án
            list_ans = ["\\True " + da_dung, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # Vẽ hình TikZ
            tikz_code = """\\begin{center} \\begin{tikzpicture}[scale=1, line width=1pt, line cap=round, line join=round]
            \\coordinate (A) at (0,0);
            \\coordinate (B) at (-1.5,-1.2);
            \\coordinate (D) at (2.5,0);
            \\coordinate (C) at ($(B)+(D)-(A)$);
            \\coordinate (S) at (0,3);
            \\draw [line width=1pt] (S)--(B)--(C)--(D)--(S)--(C);
            \\draw [dashed, line width=1pt] (S)--(A)--(B) (A)--(D) (A)--(C);
            \\draw (A) node[left] {$A$} (B) node[below left] {$B$} (C) node[below right] {$C$} (D) node[right] {$D$} (S) node[above] {$S$};
            \\tkzMarkRightAngle(S,A,B)
            \\tkzMarkRightAngle(S,A,D)
            \\end{tikzpicture} \\end{center}"""

            # Nội dung câu hỏi
            noidungcauhoi = ("Cho hình chóp $S.ABCD$, đáy $ABCD$ là hình vuông cạnh $a$ và $SA \\perp \\left( ABCD \\right)$. Biết $SA = %s$. Góc giữa $SC$ và $\\left( ABCD \\right)$ bằng bao nhiêu?" % sa_latex)

            # Lời giải chi tiết
            loigiai = ("Ta có $SA \\perp \\left( ABCD \\right)$.\\\\ "
                       "Do đó $AC$ là hình chiếu của $SC$ lên mặt phẳng $\\left( ABCD \\right)$.\\\\ "
                       "$\\Rightarrow \\left( SC, \\left( ABCD \\right) \\right) = \\left( SC, AC \\right) = \\widehat{SCA}$.\\\\ "
                       "Vì $ABCD$ là hình vuông cạnh $a$ nên đường chéo $AC = a\\sqrt{2}$.\\\\ "
                       "Xét tam giác $SAC$ vuông tại $A$, ta có $\\tan \\widehat{SCA} = \\frac{SA}{AC} = \\frac{%s}{a\\sqrt{2}} = %s$.\\\\ "
                       "$\\Rightarrow \\widehat{SCA} = %s^\\circ$.\\\\ "
                       "Vậy góc giữa $SC$ và $\\left( ABCD \\right)$ là $%s^\\circ$." 
                       % (sa_latex, "v_tam", goc_chon, goc_chon))
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(goc_chon))

            # Thay thế giá trị tan tùy theo góc để lời giải logic
            if goc_chon == 30:
                loigiai = loigiai.replace("v_tam", "\\frac{\\sqrt{3}}{3}")
            elif goc_chon == 45:
                loigiai = loigiai.replace("v_tam", "1")
            else:
                loigiai = loigiai.replace("v_tam", "\\sqrt{3}")

            # Xuất nội dung theo mẫu (không dùng tiền tố r)
            content = ("\\begin{minipage}{\\textwidth} \n"
                       "\\begin{ex}\n"
                       + noidungcauhoi + str(dapan)+
                       "\\loigiai{"+ tikz_code + loigiai + "}\n"
                       "\\end{ex}\n"
                       "\\end{minipage} \n\n")
            return content

