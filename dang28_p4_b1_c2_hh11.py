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


def bt_dang28_p4_b1_c2_hh11(self):
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Đáp án đúng
                kq = '60^\\circ'

                # Danh sách các phương án nhiễu
                s = ['$30^\\circ$', '$45^\\circ$', '$90^\\circ$', '$120^\\circ$', '$150^\\circ$']

                # Chọn ngẫu nhiên 3 đáp án sai từ danh sách s
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Đảm bảo đáp án sai không trùng với đáp án đúng (dù logic góc này hiếm khi trùng)
                if das1 == '$60^\\circ$': das1 = s[3]
                if das2 == '$60^\\circ$': das2 = s[3]
                if das3 == '$60^\\circ$': das3 = s[3]

                # Câu hỏi (Sử dụng TikZ để vẽ hình lập phương)
                # Lưu ý: Không dùng tiền tố r ở biến content theo yêu cầu
                noidungcauhoi = ('''Cho hình lập phương $ABCD.A'B'C'D'$ có $I, J$ lần lượt là trung điểm của $BC$ và $BB'$. Tính góc giữa hai đường thẳng $AC$ và $IJ$.''')

                # Các đáp án
                da_d = ('\\True $' + str(kq) + '$')
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Trộn ngẫu nhiên các phương án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết
                loigiai = ('''\\begin{center}
                \\begin{tikzpicture}[scale=2, line join=round, line cap=round, >=stealth]
                    \\coordinate (A) at (0,1);
                    \\coordinate (B) at (1,1);
                    \\coordinate (C) at (1.4,1.3);
                    \\coordinate (D) at (0.4,1.3);
                    \\coordinate (A1) at (0,0);
                    \\coordinate (B1) at (1,0);
                    \\coordinate (C1) at (1.4,0.3);
                    \\coordinate (D1) at (0.4,0.3);
                    \\draw (A) -- (B) -- (B1) -- (A1) -- cycle;
                    \\draw (B) -- (C) -- (C1) -- (B1);
                    \\draw (A) -- (D) -- (C);
                    \\draw[dashed] (A1) -- (D1) -- (C1);
                    \\draw[dashed] (D) -- (D1);
                    \\coordinate (I) at ($(B)!0.5!(C)$);
                    \\coordinate (J) at ($(B)!0.5!(B1)$);
                    \\draw (A) -- (C);
                    \\draw (I) -- (J);
                    \\draw (A) -- (B1);
                    \\draw (B1) -- (C);
                    \\node[left] at (A) {$A$};
                    \\node[below left] at (B) {$B$};
                    \\node[right] at (C) {$C$};
                    \\node[above] at (D) {$D$};
                    \\node[left] at (A1) {$A'$};
                    \\node[below] at (B1) {$B'$};
                    \\node[right] at (C1) {$C'$};
                    \\node[above right] at (D1) {$D'$};
                    \\node[above] at (I) {$I$};
                    \\node[left] at (J) {$J$};
                \\end{tikzpicture}
                \\end{center}Vì $I, J$ lần lượt là trung điểm của $BC$ và $BB'$ nên $IJ$ là đường trung bình của tam giác $B'BC$. \\\\
            Suy ra $IJ \\parallel B'C$. \\\\
            Khi đó, góc giữa hai đường thẳng $AC$ và $IJ$ bằng góc giữa hai đường thẳng $AC$ và $B'C$:
            $$(IJ, AC) = (B'C, AC).$$
            Xét tam giác $ACB'$, ta có:
            \\begin{itemize}
                \\item $AC$ là đường chéo của hình vuông $ABCD$.
                \\item $AB'$ là đường chéo của hình vuông $ABB'A'$.
                \\item $CB'$ là đường chéo của hình vuông $BCC'B'$.
            \\end{itemize}
            Vì $ABCD.A'B'C'D'$ là hình lập phương nên các mặt là các hình vuông bằng nhau, do đó các đường chéo của chúng cũng bằng nhau: $AC = AB' = CB'$. \\\\
            Suy ra tam giác $ACB'$ là tam giác đều. \\\\
            Vậy $(IJ, AC) = (B'C, AC) = \\widehat{ACB'} = 60^\\circ$.''')

            # B4: Xuất nội dung theo cấu trúc mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

