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


def bt_dang47_p4_b3_c2_hh11(self):
            # Khai báo biến
            # Khai báo các thông số random
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hệ số k cho cạnh a (ví dụ k từ 1 đến 5)
                k = random.randint(1, 5)

                # Tính toán các giá trị dựa trên k
                # AB = 2ka, SA = ka*sqrt(2)
                val_ab = 2 * k
                val_sa_sq = 2 * k**2 

                # AH = AB * cos(60) = 2ka * 1/2 = ka
                # BH = AB * sin(60) = 2ka * sqrt(3)/2 = ka*sqrt(3)
                val_ah = k
                val_bh_sq = 3 * k**2 

                # SH^2 = SA^2 + AH^2 = 2k^2 + k^2 = 3k^2
                # Vì SH^2 = BH^2 nên SH = BH. Tam giác SBH vuông cân tại H.
                dap_an_dung = '45^\\circ'

                # Các phương án nhiễu
                s = ['30^\\circ', '60^\\circ', '90^\\circ', '15^\\circ', '75^\\circ']
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Định dạng hiển thị biến a
                a_ab = str(val_ab) + 'a' if val_ab != 1 else 'a'
                a_sa = str(k) + 'a\\sqrt{2}' if k != 1 else 'a\\sqrt{2}'
                a_ah = str(k) + 'a' if k != 1 else 'a'
                a_bh = str(k) + 'a\\sqrt{3}' if k != 1 else 'a\\sqrt{3}'
                a_sh = str(k) + 'a\\sqrt{3}' if k != 1 else 'a\\sqrt{3}'

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho hình chóp $S.ABC$ có đáy là tam giác vuông tại $B$, cạnh bên $SA$ vuông góc với mặt phẳng đáy, $AB = %s$, $\\widehat{BAC} = 60^\\circ$ và $SA = %s$. Tính góc giữa đường thẳng $SB$ và mặt phẳng $\\left( SAC \\right)$.'''
                                 % (a_ab, a_sa))

                # Các đáp án
                da_d = '\\True $' + dap_an_dung + '$'
                da_s1 = '$' + das1 + '$'
                da_s2 = '$' + das2 + '$'
                da_s3 = '$' + das3 + '$'

                list_ans = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_ans)

                # TikZ code vẽ hình giống 100% ảnh mẫu
                hinh_ve = r'''\begin{center}
            \begin{tikzpicture}[scale=1, font=\footnotesize, line join=round, line cap=round, >=stealth]
                % Định nghĩa tọa độ
                \coordinate (S) at (0,4);
                \coordinate (A) at (0,0);
                \coordinate (C) at (4,0);
                \coordinate (B) at (1.5,-1.5);
                \coordinate (H) at (1.5,0); % Hình chiếu của B lên AC
                \draw [dashed, line width=0.6pt] (A)--(C);
                \draw [dashed, line width=0.6pt] (S)--(H);
                \draw [dashed, line width=0.6pt] (B)--(H);
                \draw [line width=0.8pt] (S)--(A)--(B)--(C)--cycle;
                \draw [line width=0.8pt] (S)--(B);
                \draw (S) node [above] {$S$};
                \draw (A) node [left] {$A$};
                \draw (C) node [right] {$C$};
                \draw (B) node [below] {$B$};
                \draw (H) node [above right] {$H$};
            \end{tikzpicture}
            \end{center}'''

                # Nội dung lời giải
                loigiai = (hinh_ve +'''Trong mặt phẳng $\\left( ABC \\right)$ kẻ $BH \\perp AC$ tại $H$. \\\\
                              Mà $BH \\perp SA$ (do $SA \\perp \\left( ABC \\right)$). \\\\
                              Suy ra $BH \\perp \\left( SAC \\right)$. \\\\
                              Do đó $SH$ là hình chiếu vuông góc của $SB$ lên mặt phẳng $(SAC)$. \\\\
                              Góc giữa đường thẳng $SB$ và mặt phẳng $\\left( SAC \\right)$ bằng $\\widehat{BSH}$. \\\\
                              Xét tam giác $ABH$ vuông tại $H$: \\\\
                              $BH = AB \\cdot \\sin 60^\\circ = %s \\cdot \\frac{\\sqrt{3}}{2} = %s$. \\\\
                              $AH = AB \\cdot \\cos 60^\\circ = %s \\cdot \\frac{1}{2} = %s$. \\\\
                              Xét tam giác $SAH$ vuông tại $A$: \\\\
                              $SH = \\sqrt{SA^2 + AH^2} = \\sqrt{\\left( %s \\right)^2 + \\left( %s \\right)^2} = %s$. \\\\
                              Xét tam giác $SBH$ vuông tại $H$ (vì $BH \\perp \\left( SAC \\right) \\Rightarrow BH \\perp SH$) có $SH = BH = %s$. \\\\
                              Suy ra tam giác $SBH$ vuông cân tại $H$. \\\\
                              Vậy $\\widehat{BSH} = 45^\\circ$.'''
                            % (a_ab, a_bh, a_ab, a_ah, a_sa, a_ah, a_sh, a_sh))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'  + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

