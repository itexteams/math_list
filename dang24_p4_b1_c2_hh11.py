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


def bt_dang24_p4_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến và chọn ngẫu nhiên tên cạnh
            lis_canh = ['a', 'm', 'k', 'x']
            canh = random.choice(lis_canh)

            # Các phương án trả lời
            da_dung = '$60^\\circ$'
            cac_da_sai = ['$30^\\circ$', '$45^\\circ$', '$90^\\circ$']

            # Trộn đáp án
            da_d = '\\True ' + da_dung
            list_1 = [da_d] + cac_da_sai
            random.shuffle(list_1)

            # Hình vẽ TikZ
            tikz_code = ('''\\begin{center}
            \\begin{tikzpicture}[scale=0.8, line join=round, line cap=round]
                \\coordinate (A) at (0,0);
                \\coordinate (B) at (-1.5,-1.5);
                \\coordinate (C) at (2,-1.5);
                \\coordinate (D) at (3.5,0);
                \\coordinate (S) at (1,3.5);
                \\coordinate (I) at ($(S)!0.5!(C)$);
                \\coordinate (J) at ($(B)!0.5!(C)$);
                \\draw[dashed] (S)--(A)--(B) (A)--(D);
                \\draw (S)--(B)--(C)--(D)--(S)--(C);
                \\draw[blue, thick] (I)--(J);
                \\foreach \\p/\\pos in {S/above, A/left, B/below left, C/below right, D/right, I/right, J/below}
                    \\fill (\\p) node[\\pos] {$\\p$};
            \\end{tikzpicture}
            \\end{center}''')

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có tất cả các cạnh đều bằng $%s$. Gọi $I$ và $J$ lần lượt là trung điểm của $SC$ và $BC$. Tính góc giữa hai đường thẳng $IJ$ và $CD$.
            %s''' % (latex(canh), tikz_code))

            # Nội dung lời giải chi tiết
            loigiai = ('''Trong tam giác $SBC$, ta có $I, J$ lần lượt là trung điểm của $SC$ và $BC$. \\\\
            Suy ra $IJ$ là đường trung bình của tam giác $SBC$, do đó $IJ \\parallel SB$. (1) \\\\
            Vì đáy $ABCD$ là hình vuông (do hình chóp có tất cả các cạnh bằng nhau), nên ta có $CD \\parallel AB$. (2) \\\\
            Từ (1) và (2) suy ra: $(IJ, CD) = (SB, AB) = \\widehat{SBA}$. \\\\
            Xét tam giác $SAB$ có $SA = SB = AB = %s$, nên tam giác $SAB$ là tam giác đều. \\\\
            Do đó $\\widehat{SBA} = 60^\\circ$. \\\\
            Vậy góc giữa hai đường thẳng $IJ$ và $CD$ bằng $60^\\circ$.''' % (latex(canh)))

            # Xuất câu trắc nghiệm theo đúng cấu trúc mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

