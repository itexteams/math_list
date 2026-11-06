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


def bt_dang8_p2_b1_c2_hh11(self):
            # Khai báo biến
            # Chọn ngẫu nhiên độ dài cạnh đáy a là một số nguyên từ 2 đến 6
            a_val = random.randint(2, 6)

            # Danh sách các cấu trúc tỉ lệ SA/a để tạo ra góc đẹp (30, 45, 60 độ)
            # (hệ số nhân, góc SDA, chuỗi latex của SA)
            list_config = [
                (sqrt(3), 60, "%s\\sqrt{3}" % a_val),
                (1, 45, "%s" % a_val),
                (Rational(1, 3) * sqrt(3), 30, "\\frac{%s\\sqrt{3}}{3}" % a_val)
            ]

            ratio, angle_val, sa_latex = random.choice(list_config)

            # B2: Viết lại nội dung bài toán (Nội dung câu hỏi)
            noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy là hình thoi cạnh $%s$. Cho biết $SA = %s$, $SA \\perp AB$, $SA \\perp AD$. 
            \\\\ 
            \\begin{center}
            \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round]
            \\coordinate (A) at (0,0);
            \\coordinate (D) at (3,0);
            \\coordinate (B) at (1,1);
            \\coordinate (C) at (4,1);
            \\coordinate (S) at (0,3);
            \\draw (S)--(C)--(D)--cycle;
            \\draw (S)--(C) (S)--(D) (S)--(A) (A)--(D);
            \\draw[dashed] (A)--(B) (S)--(B) (B)--(C);
            \\draw (0,0.2)--(0.2,0.2)--(0.2,0);
            \\draw (0.15,0.15)--(0.25,0.25);
            \\node at (A) [left] {$A$};
            \\node at (B) [left] {$B$};
            \\node at (C) [right] {$C$};
            \\node at (D) [right] {$D$};
            \\node at (S) [above] {$S$};
            \\end{tikzpicture}
            \\end{center}''' % (a_val, sa_latex))

            ########################################################################
            # a) Nhận biết: Góc giữa SA và AB
            ########################################################################
            nb_da_1_d = '\\True $(AB, SA) = 90^\\circ$'
            nb_da_1_s = '$(AB, SA) = 60^\\circ$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Vì $SA \\perp AB$ theo giả thiết, nên góc giữa hai đường thẳng $AB$ và $SA$ bằng $90^\\circ$.''')

            ########################################################################
            # b) Thông hiểu: Quan hệ vuông góc SA và CD
            ########################################################################
            th_da_1_d = '\\True $SA \\perp CD$'
            th_da_1_s = '$SA \\perp SC$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Ta có $\\begin{cases} SA \\perp AB \\\\ SA \\perp AD \\end{cases} \\Rightarrow SA \\perp (ABCD)$. 
            Vì $CD$ là cạnh của hình thoi nên $CD \\subset (ABCD)$, suy ra $SA \\perp CD$.''')

            ########################################################################
            # c) Vận dụng: Góc giữa đường thẳng song song
            ########################################################################
            vd_da_1_d = '\\True $(SD, BC) = (SD, AD)$'
            vd_da_1_s = '$(SD, BC) = (SD, CD)$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Do $ABCD$ là hình thoi nên $BC \\parallel AD$. 
            Suy ra góc giữa $SD$ và $BC$ bằng góc giữa $SD$ và $AD$, tức là $(SD, BC) = (SD, AD) = \\widehat{SDA}$.''')

            ########################################################################
            # d) Vận dụng cao: Tính toán số đo góc cụ thể
            ########################################################################
            vdc_da_1_d = '\\True $\\widehat{SDA} = %s^\\circ$' % angle_val
            vdc_da_1_s = '$\\widehat{SDA} = %s^\\circ$' % (90 - angle_val)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Tam giác $SAD$ vuông tại $A$ (do $SA \\perp (ABCD)$). 
            Ta có: $\\tan \\widehat{SDA} = \\frac{SA}{AD} = \\frac{%s}{%s} = %s$. 
            Từ đó suy ra $\\widehat{SDA} = %s^\\circ$.''' % (sa_latex, a_val, latex(ratio), angle_val))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # B3: Lặp đến khi đáp án có từ 1 đến 3 đúng để tăng tính ngẫu nhiên
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    break

            # Xuất nội dung theo mẫu Content yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ 
                str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(nb_sel)+'}\n'
                '{'+str(th_sel)+'}\n'
                '{'+str(vd_sel)+'}\n'
                '{'+str(vdc_sel)+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(loigiai_nb_1)+'\n'
                '\\item '+str(loigiai_th_1)+'\n'
                '\\item '+str(loigiai_vd_1)+'\n'
                '\\item '+str(loigiai_vdc_1)+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

