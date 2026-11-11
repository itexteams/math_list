
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


def bt_dang7_p4_b2_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Nội dung câu hỏi
        noidungcauhoi = (
            'Cho chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật. Gọi $M, N, E, F$ lần lượt là trọng tâm các tam giác $SAB, SBC, SCD, SDA$. Chứng minh:\\\\ \n'
            'a. Bốn điểm $M, N, E, F$ đồng phẳng. \\\\ \n'
            'b. $ME, NF, SO$ đồng quy với $O$ là tâm hình chữ nhật $ABCD$. \n'
        )
        
        # Code vẽ hình TikZ
        tikz_code = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.8, line join=round, line cap=round]\n'
            '\\coordinate (A) at (0,3);\n'
            '\\coordinate (B) at (-2,0);\n'
            '\\coordinate (C) at (4,0);\n'
            '\\coordinate (D) at (6,3);\n'
            '\\coordinate (S) at (1,8);\n'
            '\\coordinate (M\') at ($(A)!0.5!(B)$);\n'
            '\\coordinate (N\') at ($(B)!0.5!(C)$);\n'
            '\\coordinate (E\') at ($(C)!0.5!(D)$);\n'
            '\\coordinate (F\') at ($(D)!0.5!(A)$);\n'
            '\\coordinate (O) at (intersection of A--C and B--D);\n'
            '\\coordinate (M) at ($(S)!2/3!(M\')$);\n'
            '\\coordinate (N) at ($(S)!2/3!(N\')$);\n'
            '\\coordinate (E) at ($(S)!2/3!(E\')$);\n'
            '\\coordinate (F) at ($(S)!2/3!(F\')$);\n'
            '\\draw[thick] (S)--(B)--(C)--(D)--(S)--(C);\n'
            '\\draw[dashed, thick] (S)--(A)--(B);\n'
            '\\draw[dashed, thick] (A)--(D);\n'
            '\\draw[dashed, thick] (A)--(C);\n'
            '\\draw[dashed, thick] (B)--(D);\n'
            '\\draw[dashed, thick] (S)--(O);\n'
            '\\draw[dashed, thick] (M\')--(N\')--(E\')--(F\')--cycle;\n'
            '\\draw[dashed, thick] (M\')--(E\');\n'
            '\\draw[dashed, thick] (N\')--(F\');\n'
            '\\draw[dashed, thick] (S)--(M\');\n'
            '\\draw (S)--(N\');\n'
            '\\draw (S)--(E\');\n'
            '\\draw[dashed, thick] (S)--(F\');\n'
            '\\draw[dashed, thick] (M)--(N)--(E)--(F)--cycle;\n'
            '\\draw[dashed, thick] (M)--(E);\n'
            '\\draw[dashed, thick] (N)--(F);\n'
            '\\fill (S) circle (1.5pt) node[above] {$S$};\n'
            '\\fill (A) circle (1.5pt) node[left] {$A$};\n'
            '\\fill (B) circle (1.5pt) node[below left] {$B$};\n'
            '\\fill (C) circle (1.5pt) node[below right] {$C$};\n'
            '\\fill (D) circle (1.5pt) node[right] {$D$};\n'
            '\\fill (M\') circle (1.5pt) node[left] {$M\'$};\n'
            '\\fill (N\') circle (1.5pt) node[below] {$N\'$};\n'
            '\\fill (E\') circle (1.5pt) node[right] {$E\'$};\n'
            '\\fill (F\') circle (1.5pt) node[above right] {$F\'$};\n'
            '\\fill (O) circle (1.5pt) node[below right] {$O$};\n'
            '\\fill (M) circle (1.5pt) node[left] {$M$};\n'
            '\\fill (N) circle (1.5pt) node[right] {$N$};\n'
            '\\fill (E) circle (1.5pt) node[right] {$E$};\n'
            '\\fill (F) circle (1.5pt) node[above] {$F$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        )

        # Nội dung lời giải
        loigiai = (
            tikz_code +
            '\\begin{enumEX}[a)]{1} \n'
            '\\item Gọi $M\', N\', E\', F\'$ lần lượt là trung điểm của $AB, BC, CD, DA$. \\\\ \n'
            'Ta có: \\\\ \n'
            '$\\dfrac{SM}{SM\'} = \\dfrac{2}{3}; \\dfrac{SN}{SN\'} = \\dfrac{2}{3}$ (tính chất trọng tâm tam giác) \\\\ \n'
            '$\\Rightarrow \\dfrac{SM}{SM\'} = \\dfrac{SN}{SN\'}$ \\\\ \n'
            '$\\Rightarrow MN \\parallel M\'N\'$ (Định lý Ta $-$ lét) \\\\ \n'
            'Tương tự: $\\dfrac{SE}{SE\'} = \\dfrac{SF}{SF\'}$ \\\\ \n'
            '$\\Rightarrow EF \\parallel E\'F\'$ (Định lý Ta $-$ lét) \\\\ \n'
            'Lại có: $\\begin{cases} M\'N\' \\parallel AC \\\\ E\'F\' \\parallel AC \\end{cases}$ (tính chất đường trung bình) \\\\ \n'
            '$\\Rightarrow M\'N\' \\parallel E\'F\'$ \\\\ \n'
            'Do đó: $MN \\parallel EF$. \\\\ \n'
            'Vậy bốn điểm $M, N, E, F$ đồng phẳng. \n'
            '\\item Gọi $I$ là giao điểm của $ME$ và $NF$. \\\\ \n'
            'Dễ thấy $M\'N\'E\'F\'$ là hình bình hành và $O$ là giao điểm của $M\'E\'$ và $N\'F\'$. \\\\ \n'
            'Xét ba mặt phẳng $(M\'SE\'), (N\'SF\'), (MNEF)$ có: \\\\ \n'
            '$(M\'SE\') \\cap (N\'SF\') = SO$ \\\\ \n'
            '$(M\'SE\') \\cap (MNEF) = ME$ \\\\ \n'
            '$(N\'SF\') \\cap (MNEF) = NF$ \\\\ \n'
            '$ME \\cap NF = I$ \\\\ \n'
            'Do đó theo định lý về giao tuyến của ba mặt phẳng thì ba đường thẳng $ME, NF, SO$ đồng quy tại $I$. \n'
            '\\end{enumEX} \n'
        )

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content
