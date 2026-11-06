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


def bt_dang9_p3_b3_c2_hh11(self):
            # Khai báo biến
            # Khai báo các biến ký hiệu
            a = symbols('a')

            # B3-Suy nghĩ tìm cách random bài toán
            case = random.choice(['60', '45', '30'])

            if case == '60':
                k = 1 
                m = 2 
                str_ab = "a"
                val_sb = 2*a
                kq_goc = 60
            elif case == '45':
                k = 1
                m = sqrt(2)
                str_ab = "a"
                val_sb = sqrt(2)*a
                kq_goc = 45
            else: # Case 30
                k = sqrt(3)
                m = 2
                str_ab = "a\\sqrt{3}"
                val_sb = 2*a
                kq_goc = 30

            str_sb = latex(val_sb)

            # B4-Điều chỉnh các phương án sai
            dap_an_dung = str(kq_goc) + "^\\circ"
            cac_goc_khac = ["30^\\circ", "45^\\circ", "60^\\circ", "90^\\circ"]
            if dap_an_dung in cac_goc_khac:
                cac_goc_khac.remove(dap_an_dung)

            random.shuffle(cac_goc_khac)
            da_s1, da_s2, da_s3 = cac_goc_khac[0], cac_goc_khac[1], cac_goc_khac[2]



            noidungcauhoi = (
                "Cho hình chóp $S.ABCD$ có đáy là hình vuông cạnh $%s$, $SA$ vuông góc với mặt phẳng đáy và $SB = %s$. Góc giữa đường thẳng $SB$ và mặt phẳng đáy bằng bao nhiêu?"
                % (str_ab, str_sb)
            )

            # Tính toán giá trị cos để đưa vào lời giải
            # Thay Rational(k, m) bằng k/m
            val_cos = latex(k/m).replace('.', ',')

            loigiai = (r"""\begin{center} \begin{tikzpicture}[line cap=round,line join=round,x=1.0cm,y=1.0cm, scale=0.7, line width=1pt]
            \coordinate (A) at (0,0);
            \coordinate (B) at (-1.5,-1.5);
            \coordinate (C) at (2.5,-1.5);
            \coordinate (D) at (4,0);
            \coordinate (S) at (0,3.5);
            \draw [dashed] (S)--(A) (A)--(B) (A)--(D);
            \draw (S)--(B)--(C)--(D)--(S)--(C);
            \draw (0,0.3)--(0.3,0.3)--(0.3,0);
            \draw (A) node[left] {$A$};
            \draw (B) node[below left] {$B$};
            \draw (C) node[below right] {$C$};
            \draw (D) node[right] {$D$};
            \draw (S) node[above] {$S$};
            \draw [thin] (-1.1,-1.1) arc (45:75:0.5);
            \end{tikzpicture} \end{center}"""
                "Vì $SA \\perp \\left( ABCD \\right)$ nên $A$ là hình chiếu vuông góc của $S$ lên mặt phẳng $\\left( ABCD \\right)$. \\\\"
                "Do đó, hình chiếu của đường thẳng $SB$ lên mặt phẳng $\\left( ABCD \\right)$ là đường thẳng $AB$. \\\\"
                "Suy ra góc giữa đường thẳng $SB$ và mặt phẳng đáy $\\left( ABCD \\right)$ là góc giữa hai đường thẳng $SB$ và $AB$, chính là góc $\\widehat{SBA}$. \\\\"
                "Xét tam giác $SAB$ vuông tại $A$, ta có: \\\\"
                "$\\cos \\widehat{SBA} = \\frac{AB}{SB} = \\frac{%s}{%s} = %s$. \\\\"
                "Vậy $\\widehat{SBA} = %s^\\circ$. \\\\"
                "Kết luận: Góc giữa đường thẳng $SB$ và mặt phẳng đáy bằng $%s^\\circ$."
                % (str_ab, str_sb, val_cos, kq_goc, kq_goc)
            )
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(kq_goc))

            da_d = "\\True $" + dap_an_dung + "$"
            da_s1 = "$" + da_s1 + "$"
            da_s2 = "$" + da_s2 + "$"
            da_s3 = "$" + da_s3 + "$"

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

