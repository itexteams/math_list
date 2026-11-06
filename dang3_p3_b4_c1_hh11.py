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


def bt_dang3_p3_b4_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Random tỷ số k = EA/EB = FA/FS = KD/KS
        # Chọn ngẫu nhiên phân số tối giản k = m/n
        pairs = [(1, 2), (2, 3), (3, 2), (1, 3), (3, 4), (1, 4), (2, 5)]
        m, n = random.choice(pairs)

        # Định dạng phân số hiển thị
        str_ratio = "\\frac{%d}{%d}" % (m, n)

        # Hình vẽ TikZ vẽ đúng 100% theo mẫu và ảnh cung cấp
        hinhve = (
            "\\begin{center}\n"
            "        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "        \\coordinate (A) at (1.5,1.2);\n"
            "        \\coordinate (B) at (0,0);\n"
            "        \\coordinate (C) at (4.5,0);\n"
            "        \\coordinate (D) at (6,1.2);\n"
            "        \\coordinate (S) at (1.5,4.5);\n"
            "        \\coordinate (E) at ($(A)!0.6!(B)$);\n"
            "        \\coordinate (F) at ($(A)!0.6!(S)$);\n"
            "        \\coordinate (K) at ($(S)!0.4!(D)$);\n"
            "        \\coordinate (H) at ($(B)!0.6!(C)$);\n"
            "        \\coordinate (H_real) at ($(C)!0.4!(D)$);\n"
            "        \\coordinate (H) at (5.4,0.72);\n"
            "        \\coordinate (K) at (4.2,2.52);\n"
            "        \\coordinate (F) at (1.5,2.52);\n"
            "        \\coordinate (E) at (0.9,0.72);\n"
            "        \\draw[line width=1pt] (S)--(B)--(C)--(D)--(S)--(C) (K)--(H);\n"
            "        \\draw[line width=1pt, dashed] (S)--(A)--(B) (A)--(D) (E)--(F)--(K) (E)--(H);\n"
            "        \\fill (A) circle (1pt) node[right] {$A$};\n"
            "        \\fill (B) circle (1pt) node[left] {$B$};\n"
            "        \\fill (C) circle (1pt) node[below] {$C$};\n"
            "        \\fill (D) circle (1pt) node[right] {$D$};\n"
            "        \\fill (S) circle (1pt) node[above left] {$S$};\n"
            "        \\fill (E) circle (1pt) node[left] {$E$};\n"
            "        \\fill (F) circle (1pt) node[left] {$F$};\n"
            "        \\fill (K) circle (1pt) node[above right] {$K$};\n"
            "        \\fill (H) circle (1pt) node[right] {$H$};\n"
            "        \\end{tikzpicture}\n"
            "        \\end{center}"
        )

        # Số lượng khẳng định đúng là 3
        kq_str = "3"

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Gọi $E$, $F$, $K$ lần lượt là các điểm thuộc các cạnh $AB$, $SA$, $SD$ (khác đầu mút) sao cho $\\frac{EA}{EB} = \\frac{FA}{FS} = \\frac{KD}{KS} = %s$ và gọi $H$ là giao điểm của cạnh $CD$ và mặt phẳng $(EFK)$. Xét các khẳng định sau:\\\\
    (1) $EK // (SBC)$.\\\\
    (2) $KH // (SBC)$.\\\\
    (3) $EH // (SAD)$.\\\\
    (4) $FK // (SAD)$.\\\\
    Trong các khẳng định trên có tất cả bao nhiêu khẳng định đúng?
    %s'''
                         % (str_ratio, hinhve)
                         )

        # Nội dung lời giải
        loigiai = ('''Theo đề bài, ta có: $\\frac{EA}{EB} = \\frac{FA}{FS} = \\frac{KD}{KS} = %s$ suy ra $EF // SB$, $FK // AD$ hay $FK // BC$.\\\\
    Do đó, $(EFK) // (SBC)$.\\\\
    Vì $(EFK) // (SBC)$ và $(SBC) \\cap (SCD) = SC$ nên $(EFK) \\cap (SCD) = KH$, với $KH // SC$, $H \\in CD$.\\\\
    Từ đó suy ra $\\frac{EA}{EB} = \\frac{FA}{FS} = \\frac{KD}{KS} = \\frac{HD}{HC}$ hay $EH // AD$.\\\\
    Khi đó:\\\\
    (1) $EK // (SBC)$ đúng vì $EK \\subset (EFK)$ và $(EFK) // (SBC)$.\\\\
    (2) $KH // (SBC)$ đúng vì $KH \\not\\subset (SBC)$, $KH // SC$, $SC \\subset (SBC)$.\\\\
    (3) $EH // (SAD)$ đúng vì $EH \\not\\subset (SAD)$, $EH // AD$, $AD \\subset (SAD)$.\\\\
    (4) $FK // (SAD)$ sai vì $FK \\subset (SAD)$.\\\\
    Vậy có %s khẳng định đúng.'''
                   % (str_ratio, kq_str)
                   )

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = (
        '\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
        '\\loigiai{ \n' + str(loigiai) + '}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

