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


def bt_dang80_p1_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến và chọn dạng (giữ cấu trúc lisdang)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thông thường bài toán hình học dùng biến a, ta giữ nguyên để đảm bảo tính tổng quát
                # Random các phương án sai xung quanh các giá trị góc đặc biệt
                dap_an_dung = '60^\\circ'

                ds_sai = ['0^\\circ', '120^\\circ', '90^\\circ', '30^\\circ', '45^\\circ', '150^\\circ']
                random.shuffle(ds_sai)

                da_s1 = ds_sai[0]
                da_s2 = ds_sai[1]
                da_s3 = ds_sai[2]

                # Nội dung câu hỏi (sử dụng TikZ để vẽ hình như yêu cầu)
                noidungcauhoi = ('''Cho tứ diện $S.ABC$ có $SA = SB = SC = AB = AC = a; BC = a\\sqrt{2}$. Góc giữa hai đường thẳng $AB$ và $SC$ bằng''')

                # Các đáp án
                da_d = ('\\True $' + dap_an_dung + '$')
                da_s1_f = ('$' + da_s1 + '$')
                da_s2_f = ('$' + da_s2 + '$')
                da_s3_f = ('$' + da_s3 + '$')

                list_1 = [da_d, da_s1_f, da_s2_f, da_s3_f]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''\\begin{center}
                \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round]
                    \\coordinate (A) at (0,1);
                    \\coordinate (B) at (3,1);
                    \\coordinate (C) at (1,-0.5);
                    \\coordinate (S) at (1.5,3);
                    \\coordinate (M) at ($(B)!0.5!(C)$);
                    \\coordinate (N) at ($(S)!0.5!(B)$);
                    \\coordinate (P) at ($(S)!0.5!(A)$);
                    \\draw (S)--(A)--(C)--(B)--(S)--(C) (P)--(C) (N)--(M);
                    \\draw[dashed] (A)--(B);
                    \\draw[dashed] (P)--(N)  (M)--(P);
                    \\draw[dashed]  (B)--(P);
                    \\fill (A)  node[left]{$A$};
                    \\fill (B)  node[right]{$B$};
                    \\fill (C)  node[below]{$C$};
                    \\fill (S)  node[above]{$S$};
                    \\fill (M)  node[below right]{$M$};
                    \\fill (N)  node[right]{$N$};
                    \\fill (P)  node[left]{$P$};
                \\end{tikzpicture}
                \\end{center} Gọi $M, N, P$ lần lượt là trung điểm của $BC, SB, SA$. \\\\
                Góc giữa $AB$ và $SC$ là góc giữa $PN$ và $MN$ (do $PN \\parallel AB$ và $MN \\parallel SC$). \\\\
                Ta có: $MN = \\frac{SC}{2} = \\frac{a}{2}$; $NP = \\frac{AB}{2} = \\frac{a}{2}$. \\\\
                Xét tam giác $SAC$ đều cạnh $a$ nên trung tuyến $PC = \\frac{a\\sqrt{3}}{2}$. \\\\
                Tương tự tam giác $SAB$ đều cạnh $a$ nên trung tuyến $BP = \\frac{a\\sqrt{3}}{2}$. \\\\
                Xét tam giác $PBC$ có $BP = PC = \\frac{a\\sqrt{3}}{2}$ nên tam giác $PBC$ cân tại $P$. \\\\
                Vì $M$ là trung điểm $BC$ nên $PM \\perp BC$. \\\\
                Trong tam giác vuông $PMC$, ta có: \\\\
                $PM = \\sqrt{PC^2 - CM^2} = \\sqrt{\\left(\\frac{a\\sqrt{3}}{2}\\right)^2 - \\left(\\frac{a\\sqrt{2}}{2}\\right)^2} = \\sqrt{\\frac{3a^2}{4} - \\frac{2a^2}{4}} = \\sqrt{\\frac{a^2}{4}} = \\frac{a}{2}$. \\\\
                Suy ra tam giác $MNP$ là tam giác đều (vì $MN = NP = PM = \\frac{a}{2}$) $\\Rightarrow \\widehat{MNP} = 60^\\circ$. \\\\
                Vậy góc giữa $AB$ và $SC$ bằng $60^\\circ$.''')

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

