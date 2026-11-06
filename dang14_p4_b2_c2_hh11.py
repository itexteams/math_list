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


def bt_dang14_p4_b2_c2_hh11(self):
            # Khai báo biến
            # Ngẫu nhiên giá trị cạnh
            a = random.randint(2, 5)
            b = random.randint(2, 5)
            while b == a:
                b = random.randint(2, 5)

            # B4: Điều chỉnh các phương án sai
            # Đáp án đúng luôn là BC vuông góc AD
            da_d = "\\True $BC \\perp AD$"

            # Danh sách các phương án sai tiềm năng
            s_list = [
                "$AC \\perp BD$",
                "$AB \\perp (BCD)$",
                "$DC \\perp (ABC)$",
                "$AD \\perp (ABC)$",
                "$BC \\perp (ABD)$",
                "$AB \\perp CD$"
            ]
            random.shuffle(s_list)

            # Chọn 3 đáp án sai từ danh sách đã trộn
            da_s1 = s_list[0]
            da_s2 = s_list[1]
            da_s3 = s_list[2]

            # Trộn thứ tự các đáp án để xuất ra content
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Hình vẽ TikZ
            tikz_hinh = """\\begin{center}
            \\begin{tikzpicture}[line width=1pt, scale=1]
                \\coordinate (A) at (1.5, 3.5);
                \\coordinate (B) at (0, 0);
                \\coordinate (C) at (4, 0);
                \\coordinate (D) at (1, -1);
                \\coordinate (H) at (2, 0); % Trung điểm BC
                \\draw (A)--(B)--(D)--(C)--(A)--(D);
                \\draw[dashed] (B)--(C);
                \\draw[dashed] (A)--(H);
                \\draw[dashed] (D)--(H);
                \\node[above] at (A) {$A$};
                \\node[left] at (B) {$B$};
                \\node[right] at (C) {$C$};
                \\node[below] at (D) {$D$};
                \\node[above right] at (H) {$H$};
            \\end{tikzpicture}
            \\end{center}"""

            # B2: Viết nội dung câu hỏi và lời giải chi tiết
            noidungcauhoi = ("Cho tứ diện $ABCD$ có $AB = AC$ và $DB = DC$. Chứng minh $BC \\perp AD$." 
                             )

            loigiai = ("""%s
            Xét tam giác $ABC$ có $AB = AC = %s$ nên tam giác $ABC$ cân tại $A$. \\\\
            Gọi $H$ là trung điểm của cạnh $BC$. Trong tam giác cân, đường trung tuyến đồng thời là đường cao, do đó ta có $AH \\perp BC$. (1) \\\\
            Xét tam giác $DBC$ có $DB = DC = %s$ nên tam giác $DBC$ cân tại $D$. \\\\
            Vì $H$ là trung điểm của $BC$, nên đường trung tuyến $DH$ cũng đồng thời là đường cao, do đó ta có $DH \\perp BC$. (2) \\\\
            Từ (1) và (2) ta suy ra $BC$ vuông góc với mặt phẳng chứa hai đường thẳng $AH$ và $DH$, tức là $BC \\perp (ADH)$. \\\\
            Mà đường thẳng $AD$ nằm trong mặt phẳng $(ADH)$, suy ra $BC \\perp AD$. \\\\
            Vậy $BC \\perp AD$.""" 
                       % (tikz_hinh, latex(a), latex(b)))

            # Xuất câu trắc nghiệm theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

