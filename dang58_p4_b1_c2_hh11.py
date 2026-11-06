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


def bt_dang58_p4_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến và thiết lập ngẫu nhiên
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Đáp án đúng
                kq = '45^\\circ'

                # Các đáp án sai ngẫu nhiên
                s = ['30^\\circ', '60^\\circ', '90^\\circ', '120^\\circ', '150^\\circ', '75^\\circ']
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho hình lập phương $ABCD.A'B'C'D'$. Gọi $M$, $N$, $P$ lần lượt là trung điểm các cạnh $AB$, $BC$, $C'D'$. Tính góc giữa hai đường thẳng $MN$ và $AP$.''')

                # Các đáp án
                da_d = ('\\True $' + str(kq) + '$')
                da_s1 = '$' + str(das1) + '$'
                da_s2 = '$' + str(das2) + '$'
                da_s3 = '$' + str(das3) + '$'

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Hình vẽ TikZ
                hinh_ve = ('''\\begin{center}
            \\begin{tikzpicture}[scale=2, line join=round, line cap=round]|
                \\coordinate (A) at (0,0,0);
                \\coordinate (B) at (2,0,0);
                \\coordinate (C) at (2,0,2);
                \\coordinate (D) at (0,0,2);
                \\coordinate (A1) at (0,2,0);
                \\coordinate (B1) at (2,2,0);
                \\coordinate (C1) at (2,2,2);
                \\coordinate (D1) at (0,2,2);
                \\coordinate (M) at ($(A)!0.5!(B)$);
                \\coordinate (N) at ($(B)!0.5!(C)$);
                \\coordinate (P) at ($(C1)!0.5!(D1)$);
                \\draw (D)--(C)--(C1)--(D1)--cycle;
                \\draw (A1)--(B1)--(C1);
                \\draw (A1)--(D1);
                \\draw (B1)--(B)--(C) (C1)--(N);
                \\draw[dashed] (A)--(B) (A)--(D) (A)--(A1);
                \\draw[dashed] (M)--(N);
                \\draw[dashed] (A)--(P) (M)--(C1) ;
                \\fill (A) node[left]{$A$};
                \\fill (B) node[right]{$B$};
                \\fill (C) node[right]{$C$};
                \\fill (D) node[left]{$D$};
                \\fill (A1) node[left]{$A'$};
                \\fill (B1) node[right]{$B'$};
                \\fill (C1) node[right]{$C'$};
                \\fill (D1) node[left]{$D'$};
                \\fill (M) node[below]{$M$};
                \\fill (N) node[right]{$N$};
                \\fill (P) node[above]{$P$};
            \\end{tikzpicture}
            \\end{center}''').replace('|', '')

                # Nội dung lời giải
                loigiai = ('''Ta có tứ giác $AMC'P$ là hình bình hành (vì $AP$ song song và bằng $MC'$) nên $AP \\parallel MC'$. \\\\
                Suy ra $(MN, AP) = (MN, MC') = \\widehat{NMC'}$. \\\\
                Gọi cạnh hình lập phương có độ dài bằng $a$. \\\\
                Xét tam giác $C'CM$ vuông tại $C$ ta có \\\\ $C'M = \\sqrt{C'C^2 + MC^2} = \\sqrt{C'C^2 + BC^2 + MB^2} = \\sqrt{a^2 + a^2 + \\left(\\frac{a}{2}\\right)^2} = \\frac{3a}{2}$. \\\\
                Xét tam giác $C'CN$ vuông tại $C$ có $C'N = \\sqrt{C'C^2 + CN^2} = \\sqrt{a^2 + \\left(\\frac{a}{2}\\right)^2} = \\frac{\\sqrt{5}a}{2}$. \\\\
                Mà $MN = \\frac{AC}{2} = \\frac{a\\sqrt{2}}{2}$. \\\\
                Xét tam giác $C'MN$ có:
                $$\\cos \\widehat{NMC'} = \\frac{MC'^2 + MN^2 - C'N^2}{2 \\cdot MC' \\cdot MN} = \\frac{\\left(\\frac{3a}{2}\\right)^2 + \\left(\\frac{a\\sqrt{2}}{2}\\right)^2 - \\left(\\frac{\\sqrt{5}a}{2}\\right)^2}{2 \\cdot \\frac{3a}{2} \\cdot \\frac{a\\sqrt{2}}{2}} = \\frac{\\sqrt{2}}{2}.$$
                $\\Rightarrow \\widehat{NMC'} = 45^\\circ \\Rightarrow (MN, AP) = 45^\\circ$.''')

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(hinh_ve)+ str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

