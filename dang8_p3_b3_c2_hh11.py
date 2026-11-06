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


def bt_dang8_p3_b3_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            a = symbols('a')
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random tỉ lệ k để mở rộng bài toán
                k = randint(1, 4)

                # Thiết lập độ dài AB và BC để AC luôn là một số đẹp (AC = 2*k*a)
                # Trong bài gốc: AB = a*sqrt(3), BC = a => AC = 2a
                val_AB = k * sqrt(3) * a
                val_BC = k * a
                val_AC = 2 * k * a

                # Bước 2: Random góc mục tiêu (30, 45, 60 độ)
                list_goc = [30, 45, 60]
                goc_dung = random.choice(list_goc)

                # Tính toán SA dựa trên góc chọn
                if goc_dung == 30:
                    # tan(30) = 1/sqrt(3) => SA = AC * 1/sqrt(3) = 2*k*a/sqrt(3) = (2*k*sqrt(3)/3)*a
                    val_SA = Rational(2 * k, 3) * sqrt(3) * a
                    tan_val = '\\frac{\\sqrt{3}}{3}'
                elif goc_dung == 45:
                    # tan(45) = 1 => SA = AC = 2*k*a
                    val_SA = 2 * k * a
                    tan_val = '1'
                else: # 60 độ
                    # tan(60) = sqrt(3) => SA = AC * sqrt(3) = 2*k*sqrt(3)*a
                    val_SA = 2 * k * sqrt(3) * a
                    tan_val = '\\sqrt{3}'

                # Đáp án đúng
                kq_dung = '%s^\\circ' % goc_dung

                # Các phương án sai (không trùng đáp án đúng)
                cac_goc_sai = [30, 45, 60, 90]
                cac_goc_sai.remove(goc_dung)

                da_d = '\\True $%s$' % kq_dung
                da_s1 = '$%s^\\circ$' % cac_goc_sai[0]
                da_s2 = '$%s^\\circ$' % cac_goc_sai[1]
                da_s3 = '$%s^\\circ$' % cac_goc_sai[2]

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # TikZ vẽ hình (S.ABC với SA vuông góc đáy, tam giác ABC vuông tại B)
                hinh_ve = ('''\\begin{center}
            \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round]
                \\coordinate (A) at (0,0);
                \\coordinate (B) at (1.2,-1);
                \\coordinate (C) at (3.5,0);
                \\coordinate (S) at (0,3);
                \\draw[line width=1pt, dashed] (A)--(C);
                \\draw[line width=1pt] (S)--(A)--(B)--(S)--(C)--(B);
                \\tkzMarkRightAngle[size=0.2](S,A,C)
                \\tkzMarkRightAngle[size=0.2](A,B,C)
                \\draw (S) node[above]{$S$};
                \\draw (A) node[left]{$A$};
                \\draw (B) node[below]{$B$};
                \\draw (C) node[right]{$C$};
            \\end{tikzpicture}
            \\end{center}''')

                # Câu hỏi
                noidungcauhoi = ('''Cho hình chóp $S.ABC$ có $SA$ vuông góc với mặt phẳng $\\left( ABC \\right)$, $SA = %s$, tam giác $ABC$ vuông tại $B$, $AB = %s$ và $BC = %s$. Góc giữa đường thẳng $SC$ và mặt phẳng $\\left( ABC \\right)$ bằng bao nhiêu?'''
                                 % (latex(val_SA).replace('.', ','), 
                                    latex(val_AB).replace('.', ','), 
                                    latex(val_BC).replace('.', ',')))

                # Lời giải chi tiết
                loigiai = ('''%s
            Ta thấy hình chiếu vuông góc của $SC$ lên mặt phẳng $\\left( ABC \\right)$ là $AC$ nên góc giữa đường thẳng $SC$ và mặt phẳng $\\left( ABC \\right)$ là góc giữa hai đường thẳng $SC$ và $AC$, hay là góc $\\widehat{SCA}$.\\\\
            Xét tam giác $ABC$ vuông tại $B$, ta có:
            $AC = \\sqrt{AB^2 + BC^2} = \\sqrt{\\left( %s \\right)^2 + \\left( %s \\right)^2} = %s$.\\\\
            Xét tam giác $SCA$ vuông tại $A$, ta có:
            $\\tan \\widehat{SCA} = \\frac{SA}{AC} = \\frac{1}{%s} \\cdot %s = %s$.\\\\
            Vậy $\\widehat{SCA} = %s^\\circ$.\\\\
            Góc giữa đường thẳng $SC$ và mặt phẳng $\\left( ABC \\right)$ bằng $%s^\\circ$.'''
                           % (hinh_ve, 
                              latex(val_AB).replace('.', ','), 
                              latex(val_BC).replace('.', ','), 
                              latex(val_AC).replace('.', ','), 
                              latex(val_AC).replace('.', ','), 
                              latex(val_SA).replace('.', ','), 
                              tan_val, 
                              goc_dung, goc_dung))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(goc_dung))

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

