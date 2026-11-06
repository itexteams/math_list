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


def bt_dang7_p3_b3_c2_hh11(self):
            # Khai báo biến
            # Cấu trúc: (latex_canh_ben, gia_tri_goc)
            lis_data = [
                ('\\sqrt{2}a', 60),
                ('a', 45),
                ('\\frac{\\sqrt{6}}{3}a', 30)
            ]

            data = random.choice(lis_data)
            canh_ben_tex = data[0]
            kq_goc = data[1]

            # Các đáp án trắc nghiệm
            da_dung = '$' + str(kq_goc) + '^\\circ$'
            # Tạo danh sách các phương án nhiễu (không trùng đáp án đúng)
            cac_goc_khac = [30, 45, 60, 75, 90, 15]
            if kq_goc in cac_goc_khac:
                cac_goc_khac.remove(kq_goc)

            random.shuffle(cac_goc_khac)
            da_s1 = '$' + str(cac_goc_khac[0]) + '^\\circ$'
            da_s2 = '$' + str(cac_goc_khac[1]) + '^\\circ$'
            da_s3 = '$' + str(cac_goc_khac[2]) + '^\\circ$'

            # Trộn đáp án
            list_1 = ['\\True ' + da_dung, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Hình vẽ TikZ
            tikz_code = '''\\begin{center} \\begin{tikzpicture}[scale=0.8, line join=round, line cap=round]
                \\coordinate (A) at (0,0);
                \\coordinate (B) at (1.5,1.2);
                \\coordinate (D) at (4,0);
                \\coordinate (C) at ($(B)+(D)-(A)$);
                \\coordinate (O) at ($(A)!0.5!(C)$);
                \\coordinate (S) at ($(O)+(0,4)$);
                \\draw[dashed, line width=1pt] (S)--(O) (A)--(C) (B)--(D) (A)--(B) (B)--(C);
                \\draw[line width=1pt] (S)--(A) (S)--(D) (S)--(C) (A)--(D) (D)--(C);
                \\draw (O)++(0,0.2)--++(0.2,0)--++(0,-0.2);
                \\draw (O)++(-0.15,0.12)--++(0.15,0.12)--++(0.15,-0.12);
                \\draw (A)++(0.4,0) arc (0:35:0.6);
                \\node at (A) [left] {$A$};
                \\node at (B) [above left] {$B$};
                \\node at (C) [right] {$C$};
                \\node at (D) [below right] {$D$};
                \\node at (S) [above] {$S$};
                \\node at (O) [below] {$O$};
            \\end{tikzpicture} \\end{center}'''

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình chóp tứ giác đều $S.ABCD$ có cạnh đáy bằng $a$, cạnh bên bằng $%s$. Góc giữa đường thẳng $SA$ và mặt phẳng đáy bằng bao nhiêu?''' 
                             % (canh_ben_tex))

            # Nội dung lời giải chi tiết
            loigiai = ('''\\begin{center} \\begin{tikzpicture}[scale=0.8, line join=round, line cap=round]
                \\coordinate (A) at (0,0);
                \\coordinate (B) at (1.5,1.2);
                \\coordinate (D) at (4,0);
                \\coordinate (C) at ($(B)+(D)-(A)$);
                \\coordinate (O) at ($(A)!0.5!(C)$);
                \\coordinate (S) at ($(O)+(0,4)$);
                \\draw[dashed, line width=1pt] (S)--(O) (A)--(C) (B)--(D) (A)--(B) (B)--(C) (S)--(B);
                \\draw[line width=1pt] (S)--(A) (S)--(D) (S)--(C) (A)--(D) (D)--(C);
                \\draw (O)++(0,0.2)--++(0.2,0)--++(0,-0.2);
                \\draw (O)++(-0.15,0.12)--++(0.15,0.12)--++(0.15,-0.12);
                \\draw (A)++(0.4,0) arc (0:35:0.6);
                \\node at (A) [left] {$A$};
                \\node at (B) [above left] {$B$};
                \\node at (C) [right] {$C$};
                \\node at (D) [below right] {$D$};
                \\node at (S) [above] {$S$};
                \\node at (O) [below] {$O$};
            \\end{tikzpicture} \\end{center}
            Gọi $O$ là tâm của hình vuông $ABCD$, ta có $SO \\perp \\left( ABCD \\right)$. \\\\
                         Góc giữa đường thẳng $SA$ và mặt phẳng đáy $\\left( ABCD \\right)$ là góc giữa $SA$ và hình chiếu $AO$ của nó trên mặt đáy. \\\\
                         Do đó $\\left( SA, \\left( ABCD \\right) \\right) = \\left( SA, AO \\right) = \\widehat{SAO} = \\alpha$. \\\\
                         Ta có đường chéo hình vuông $AC = a\\sqrt{2}$, suy ra $OA = \\frac{1}{2} AC = \\frac{a\\sqrt{2}}{2}$. \\\\
                         Xét tam giác $SAO$ vuông tại $O$, ta có: \\\\
                         $\\cos \\alpha = \\frac{OA}{SA} = \\frac{\\frac{a\\sqrt{2}}{2}}{%s} = \\cos %s^\\circ$. \\\\
                         Suy ra $\\alpha = %s^\\circ$. \\\\
                         Vậy góc giữa $SA$ và $\\left( ABCD \\right)$ bằng $%s^\\circ$.''' 
                       % (canh_ben_tex, str(kq_goc), str(kq_goc), str(kq_goc)))
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(str(kq_goc))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

