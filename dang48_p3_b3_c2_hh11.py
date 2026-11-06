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


def bt_dang48_p3_b3_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Dữ liệu cố định từ đề bài để đảm bảo tính chính xác của hình học
                # Sin alpha = sqrt(2)/4
                tu_so = sqrt(2)
                mau_so = 4
                kq_latex = "\\frac{\\sqrt{2}}{4}"

                # Các đáp án đúng
                da = "$%s$" % kq_latex

                # Các đáp án nhiễu (dựa trên các phương án A, B, C, D trong ảnh)
                s = [
                    "$\\frac{\\sqrt{2}}{2}$",
                    "$\\frac{\\sqrt{14}}{4}$",
                    "$\\frac{\\sqrt{7}}{4}$",
                    "$\\frac{\\sqrt{3}}{4}$",
                    "$\\frac{\\sqrt{6}}{4}$",
                    "$\\frac{1}{2}$"
                ]

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ("Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh $a$. Tam giác $SAB$ đều và nằm trong mặt phẳng vuông góc với đáy. Gọi $H, K$ lần lượt là trung điểm của các cạnh $AB$ và $AD$. sin của góc tạo bởi giữa hai đường thẳng $SA$ và mặt phẳng $(SHK)$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).")

                # Hình vẽ TikZ
                hinh_ve = ("""\\begin{center}
            \\begin{tikzpicture}[scale=1, line join=round, line cap=round, line width=1pt]
                \\coordinate (A) at (0,0);
                \\coordinate (B) at (5,0);
                \\coordinate (D) at (1.5,1.5);
                \\coordinate (C) at ($(B)+(D)-(A)$);
                \\coordinate (H) at ($(A)!0.5!(B)$);
                \\coordinate (K) at ($(A)!0.5!(D)$);
                \\coordinate (S) at ($(H)+(0,4)$);
                \\coordinate (E) at ($(H)!0.5!(K)$);
                \\draw [dashed]  (S)--(D)  (C)--(D) (A)--(D)  (H)--(K) (A)--(E) (S)--(E) (S)--(K);
                \\draw (S)--(A)  (S)--(C) (S)--(B) (B)--(C) (S)--(H) (A)--(B);
                \\tkzDrawPoints[size=0](S,A,B,C,D,H,K,E)
                \\node [above] at (S) {$S$};
                \\node [left] at (A) {$A$};
                \\node [below] at (B) {$B$};
                \\node [right] at (C) {$C$};
                \\node [above right] at (D) {$D$};
                \\node [below] at (H) {$H$};
                \\node [left] at (K) {$K$};
                \\node [below right] at (E) {$E$};
            \\end{tikzpicture}
            \\end{center}""")

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)
                h1=sqrt(2)/4
                number = Decimal(float(h1))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kqz=str(kq1).replace('.', ',')
                # Nội dung lời giải chi tiết
                loigiai = ("""Gọi $E$ là trung điểm của đoạn $KH$, ta có $\\triangle AHK$ vuông cân tại $A$ vì $AH = AK = \\frac{1}{2}a$ nên $AE \\perp KH$. \\\\
                            Mặt khác, vì tam giác $SAB$ đều và nằm trong mặt phẳng vuông góc với đáy nên $SH \\perp (ABCD)$, suy ra $SH \\perp AE$. \\\\
                            Ta có: $\\left\\{ \\begin{array}{l} AE \\perp SH \\\\ AE \\perp HK \\end{array} \\right. \\Rightarrow AE \\perp (SHK)$. \\\\
                            Khi đó, hình chiếu của $SA$ lên mặt phẳng $(SHK)$ là đường thẳng $SE$. \\\\
                            Suy ra $\\left( SA, (SHK) \\right) = \\left( SA, SE \\right) = \\widehat{ASE} = \\alpha$. \\\\
                            Trong tam giác vuông $AHK$, ta có $HK = \\sqrt{AH^2 + AK^2} = \\sqrt{\\left( \\frac{a}{2} \\right)^2 + \\left( \\frac{a}{2} \\right)^2} = \\frac{a\\sqrt{2}}{2}$. \\\\
                            Vì $AE$ là đường cao trong tam giác vuông cân $AHK$ nên $AE = \\frac{1}{2} HK = \\frac{a\\sqrt{2}}{4}$. \\\\
                            Xét tam giác $SEA$ vuông tại $E$, ta có $\\sin \\alpha = \\frac{AE}{SA} = \\frac{\\frac{a\\sqrt{2}}{4}}{a} = \\frac{\\sqrt{2}}{4}$. \\\\
                            Vậy $\\sin \\alpha = \\frac{\\sqrt{2}}{4} \\approx %s$."""%(kqz))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kqz))
            # Xuất nội dung theo cấu trúc yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(hinh_ve)+ str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

