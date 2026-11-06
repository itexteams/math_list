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


def bt_dang12_p1_b4_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':

        # Các đáp án trắc nghiệm (không có dấu chấm ở cuối, thay || bằng //)
        da_d = ('\\True $(MNP) // (BCD)$')
        da_s1 = '$(CMN) // (BPQ)$'
        da_s2 = '$(CMQ) // (DMN)$'
        da_s3 = '$(PQD) // (MNB)$'

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung câu hỏi (sửa lỗi gõ lặp cạnh trong ảnh thành các cạnh SA, SB, SC, SD chuẩn mực)
        noidungcauhoi = ('''%s''' % ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành, gọi $M, N, P, Q$ lần lượt là trung điểm các cạnh $SA, SB, SC, SD$. Chọn khẳng định đúng:'))

        # Hình vẽ TikZ vẽ đúng 100% như ảnh, nét vẽ 1pt, điểm 1pt, màu đen
        hinhve = ('''\\begin{center}
            \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (S) at (2.2,4.5);
            \\coordinate (A) at (2.4,1.8);
            \\coordinate (B) at (1.0,0.0);
            \\coordinate (C) at (5.0,0.0);
            \\coordinate (D) at (6.4,1.8);
            \\coordinate (M) at ($(S)!0.5!(A)$);
            \\coordinate (N) at ($(S)!0.5!(B)$);
            \\coordinate (P) at ($(S)!0.5!(C)$);
            \\coordinate (Q) at ($(S)!0.5!(D)$);
            \\draw[line width=1pt] (S)--(B)--(C)--(D)--(S)--(C) (N)--(P)--(Q);
            \\draw[line width=1pt, dashed] (S)--(A)--(B) (A)--(D) (M)--(Q) (M)--(N) (S)--(M);
            \\fill (S) circle (1pt) node[left] {$S$};
            \\fill (A) circle (1pt) node[below left] {$A$};
            \\fill (B) circle (1pt) node[below left] {$B$};
            \\fill (C) circle (1pt) node[below right] {$C$};
            \\fill (D) circle (1pt) node[right] {$D$};
            \\fill (M) circle (1pt) node[above right] {$M$};
            \\fill (N) circle (1pt) node[left] {$N$};
            \\fill (P) circle (1pt) node[right] {$P$};
            \\fill (Q) circle (1pt) node[above right] {$Q$};
            \\end{tikzpicture}
            \\end{center}''')

        # Nội dung lời giải chi tiết, rõ ràng từng bước theo bản chất bài toán và ảnh gốc
        loigiai = ('''%s
    Trong tam giác $SAB$, $MN$ là đường trung bình nên $MN // AB$.\\\\
    Vì $MN \\not\\subset (ABCD)$ và $AB \\subset (ABCD)$ nên $MN // (ABCD)$.\\\\
    Trong tam giác $SBC$, $NP$ là đường trung bình nên $NP // BC$.\\\\
    Vì $NP \\not\\subset (ABCD)$ và $BC \\subset (ABCD)$ nên $NP // (ABCD)$.\\\\
    Mặt khác $MN, NP \\subset (MNP)$ và $MN \\cap NP = \\{N\\}$.\\\\
    Do đó $(MNP) // (ABCD)$, hay $(MNP) // (BCD)$.\\\\
    Dễ dàng thấy các phương án khác là sai.'''
                   % (hinhve))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n\\choice \n' '{'+str(list_1[0])+'}\n' '{'+str(list_1[1])+'}\n' '{'+str(list_1[2])+'}\n' '{'+str(list_1[3])+'}\n' '\\loigiai{\n'+str(loigiai)+'\n}\n' '\\end{ex}\n \\end{minipage} \n\n')
    return content

