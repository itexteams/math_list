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


def bt_dang32_p3_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random số lượng ống ở hàng dưới cùng (u1) và hàng trên cùng (un)
                # un < u1, khoảng cách mỗi hàng là 1 ống
                u1 = random.randint(45, 60)
                un = random.randint(15, 25)
                gia_moi_ong = 250000

                # Số hàng n = (u1 - un) + 1
                n = u1 - un + 1

                # Tổng số ống S = (u1 + un) * n / 2
                tong_so_ong = (u1 + un) * n // 2

                # Tổng số tiền (đồng)
                tong_tien = tong_so_ong * gia_moi_ong

                # Đổi ra triệu đồng
                trieu_dong = tong_tien / 1000000

                # Làm tròn đến hàng đơn vị triệu đồng
                kq_lam_tron = int(Decimal(str(trieu_dong)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

                # Đáp án đúng
                da = '$%s$ triệu đồng' % (latex(kq_lam_tron))

                # Tạo các phương án sai (không trùng đáp án đúng)
                s = set()
                while len(s) < 3:
                    sai = kq_lam_tron + random.choice([-5, -3, -2, 2, 3, 5, 10])
                    if sai != kq_lam_tron and sai > 0:
                        s.add('$%s$ triệu đồng' % (latex(sai)))

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]
                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\tikzset {_1cq8tbgdl/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-70 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_pukzoevxm}{150bp}{rgb(0bp)=(0.5,0.59,0.62);
            		rgb(37.5bp)=(0.5,0.59,0.62);
            		rgb(45.0357164655413bp)=(1,1,1);
            		rgb(51.875bp)=(0.53,0.73,0.8);
            		rgb(58.64286150251116bp)=(0.05,0.17,0.22);
            		rgb(100bp)=(0.05,0.17,0.22)}
            	\tikzset {_nnivuyq7h/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{35.67 bp } { 0 bp }  }  \pgftransformscale{2.46 }  }}}
            	\pgfdeclareradialshading{_ti4umxxhc}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(0.02,0.11,0.12);
            		rgb(0bp)=(0.02,0.11,0.12);
            		rgb(25bp)=(0.43,0.63,0.67);
            		rgb(400bp)=(0.43,0.63,0.67)}
            	\tikzset {_8gsqgqc2b/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-70 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_jxbo9xttp}{150bp}{rgb(0bp)=(0.5,0.59,0.62);
            		rgb(37.5bp)=(0.5,0.59,0.62);
            		rgb(45.0357164655413bp)=(1,1,1);
            		rgb(51.875bp)=(0.53,0.73,0.8);
            		rgb(58.64286150251116bp)=(0.05,0.17,0.22);
            		rgb(100bp)=(0.05,0.17,0.22)}
            	\tikzset {_ga1bjgsz2/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{35.67 bp } { 0 bp }  }  \pgftransformscale{2.46 }  }}}
            	\pgfdeclareradialshading{_un8983qdx}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(0.02,0.11,0.12);
            		rgb(0bp)=(0.02,0.11,0.12);
            		rgb(25bp)=(0.43,0.63,0.67);
            		rgb(400bp)=(0.43,0.63,0.67)}
            	\tikzset {_zadpmdwqh/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-70 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_rwyc1mvtc}{150bp}{rgb(0bp)=(0.5,0.59,0.62);
            		rgb(37.5bp)=(0.5,0.59,0.62);
            		rgb(45.0357164655413bp)=(1,1,1);
            		rgb(51.875bp)=(0.53,0.73,0.8);
            		rgb(58.64286150251116bp)=(0.05,0.17,0.22);
            		rgb(100bp)=(0.05,0.17,0.22)}
            	\tikzset {_srv4fh1ip/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{35.67 bp } { 0 bp }  }  \pgftransformscale{2.46 }  }}}
            	\pgfdeclareradialshading{_c9hs7isav}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(0.02,0.11,0.12);
            		rgb(0bp)=(0.02,0.11,0.12);
            		rgb(25bp)=(0.43,0.63,0.67);
            		rgb(400bp)=(0.43,0.63,0.67)}
            	\tikzset {_h5riw555j/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-70 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_26kcivj3b}{150bp}{rgb(0bp)=(0.5,0.59,0.62);
            		rgb(37.5bp)=(0.5,0.59,0.62);
            		rgb(45.0357164655413bp)=(1,1,1);
            		rgb(51.875bp)=(0.53,0.73,0.8);
            		rgb(58.64286150251116bp)=(0.05,0.17,0.22);
            		rgb(100bp)=(0.05,0.17,0.22)}
            	\tikzset {_9mix4x0rz/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{35.67 bp } { 0 bp }  }  \pgftransformscale{2.46 }  }}}
            	\pgfdeclareradialshading{_w5o9wo1r0}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(0.02,0.11,0.12);
            		rgb(0bp)=(0.02,0.11,0.12);
            		rgb(25bp)=(0.43,0.63,0.67);
            		rgb(400bp)=(0.43,0.63,0.67)}
            	\tikzset {_a47ywyjip/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-70 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_tt0bwwccr}{150bp}{rgb(0bp)=(0.5,0.59,0.62);
            		rgb(37.5bp)=(0.5,0.59,0.62);
            		rgb(45.0357164655413bp)=(1,1,1);
            		rgb(51.875bp)=(0.53,0.73,0.8);
            		rgb(58.64286150251116bp)=(0.05,0.17,0.22);
            		rgb(100bp)=(0.05,0.17,0.22)}
            	\tikzset {_9p6uo6sx7/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{35.67 bp } { 0 bp }  }  \pgftransformscale{2.46 }  }}}
            	\pgfdeclareradialshading{_yt0ahcbye}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(0.02,0.11,0.12);
            		rgb(0bp)=(0.02,0.11,0.12);
            		rgb(25bp)=(0.43,0.63,0.67);
            		rgb(400bp)=(0.43,0.63,0.67)}
            	\tikzset {_c8jrgvosu/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-70 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_77zkno9r5}{150bp}{rgb(0bp)=(0.5,0.59,0.62);
            		rgb(37.5bp)=(0.5,0.59,0.62);
            		rgb(45.0357164655413bp)=(1,1,1);
            		rgb(51.875bp)=(0.53,0.73,0.8);
            		rgb(58.64286150251116bp)=(0.05,0.17,0.22);
            		rgb(100bp)=(0.05,0.17,0.22)}
            	\tikzset {_hu48qnyiy/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{35.67 bp } { 0 bp }  }  \pgftransformscale{2.46 }  }}}
            	\pgfdeclareradialshading{_jhj98xcb8}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(0.02,0.11,0.12);
            		rgb(0bp)=(0.02,0.11,0.12);
            		rgb(25bp)=(0.43,0.63,0.67);
            		rgb(400bp)=(0.43,0.63,0.67)}
            	\tikzset {_rp8ouo667/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-70 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_58wrmdubh}{150bp}{rgb(0bp)=(0.5,0.59,0.62);
            		rgb(37.5bp)=(0.5,0.59,0.62);
            		rgb(45.0357164655413bp)=(1,1,1);
            		rgb(51.875bp)=(0.53,0.73,0.8);
            		rgb(58.64286150251116bp)=(0.05,0.17,0.22);
            		rgb(100bp)=(0.05,0.17,0.22)}
            	\tikzset {_9hxnzzlhk/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{35.67 bp } { 0 bp }  }  \pgftransformscale{2.46 }  }}}
            	\pgfdeclareradialshading{_pbfywygmd}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(0.02,0.11,0.12);
            		rgb(0bp)=(0.02,0.11,0.12);
            		rgb(25bp)=(0.43,0.63,0.67);
            		rgb(400bp)=(0.43,0.63,0.67)}
            	\tikzset {_or93c5u4y/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-70 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_8juxqe6jq}{150bp}{rgb(0bp)=(0.5,0.59,0.62);
            		rgb(37.5bp)=(0.5,0.59,0.62);
            		rgb(45.0357164655413bp)=(1,1,1);
            		rgb(51.875bp)=(0.53,0.73,0.8);
            		rgb(58.64286150251116bp)=(0.05,0.17,0.22);
            		rgb(100bp)=(0.05,0.17,0.22)}
            	\tikzset {_i3q09xmt6/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{35.67 bp } { 0 bp }  }  \pgftransformscale{2.46 }  }}}
            	\pgfdeclareradialshading{_2bxmlrjnt}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(0.02,0.11,0.12);
            		rgb(0bp)=(0.02,0.11,0.12);
            		rgb(25bp)=(0.43,0.63,0.67);
            		rgb(400bp)=(0.43,0.63,0.67)}
            	\tikzset {_54rjonueu/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-70 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_w4luiv4xm}{150bp}{rgb(0bp)=(0.5,0.59,0.62);
            		rgb(37.5bp)=(0.5,0.59,0.62);
            		rgb(45.0357164655413bp)=(1,1,1);
            		rgb(51.875bp)=(0.53,0.73,0.8);
            		rgb(58.64286150251116bp)=(0.05,0.17,0.22);
            		rgb(100bp)=(0.05,0.17,0.22)}
            	\tikzset {_og9wjhs94/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{35.67 bp } { 0 bp }  }  \pgftransformscale{2.46 }  }}}
            	\pgfdeclareradialshading{_kp21bct93}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(0.02,0.11,0.12);
            		rgb(0bp)=(0.02,0.11,0.12);
            		rgb(25bp)=(0.43,0.63,0.67);
            		rgb(400bp)=(0.43,0.63,0.67)}
            	\tikzset {_6fufbomtd/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-70 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_zlb1kxgtb}{150bp}{rgb(0bp)=(0.5,0.59,0.62);
            		rgb(37.5bp)=(0.5,0.59,0.62);
            		rgb(45.0357164655413bp)=(1,1,1);
            		rgb(51.875bp)=(0.53,0.73,0.8);
            		rgb(58.64286150251116bp)=(0.05,0.17,0.22);
            		rgb(100bp)=(0.05,0.17,0.22)}
            	\tikzset {_mvftxkv8i/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{35.67 bp } { 0 bp }  }  \pgftransformscale{2.46 }  }}}
            	\pgfdeclareradialshading{_3vg7tiuuo}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(0.02,0.11,0.12);
            		rgb(0bp)=(0.02,0.11,0.12);
            		rgb(25bp)=(0.43,0.63,0.67);
            		rgb(400bp)=(0.43,0.63,0.67)}
            	\tikzset {_g1rg47fai/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-90 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_ulms6jrnz}{150bp}{rgb(0bp)=(0.5,0.59,0.62);
            		rgb(37.5bp)=(0.5,0.59,0.62);
            		rgb(45.0357164655413bp)=(1,1,1);
            		rgb(51.875bp)=(0.53,0.73,0.8);
            		rgb(58.64286150251116bp)=(0.05,0.17,0.22);
            		rgb(100bp)=(0.05,0.17,0.22)}
            	\tikzset {_j9godp156/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-90 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_zflny2v34}{150bp}{rgb(0bp)=(0.5,0.59,0.62);
            		rgb(37.5bp)=(0.5,0.59,0.62);
            		rgb(45.0357164655413bp)=(1,1,1);
            		rgb(51.875bp)=(0.53,0.73,0.8);
            		rgb(58.64286150251116bp)=(0.05,0.17,0.22);
            		rgb(100bp)=(0.05,0.17,0.22)}
            	\tikzset {_l8v4o66f7/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-98 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_x9fgrw5gw}{150bp}{rgb(0bp)=(0.5,0.59,0.62);
            		rgb(37.5bp)=(0.5,0.59,0.62);
            		rgb(45.0357164655413bp)=(1,1,1);
            		rgb(51.875bp)=(0.53,0.73,0.8);
            		rgb(58.64286150251116bp)=(0.05,0.17,0.22);
            		rgb(100bp)=(0.05,0.17,0.22)}
            	\tikzset {_he7v6m6cf/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-98 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_e0mv7ftih}{150bp}{rgb(0bp)=(0.5,0.59,0.62);
            		rgb(37.5bp)=(0.5,0.59,0.62);
            		rgb(45.0357164655413bp)=(1,1,1);
            		rgb(51.875bp)=(0.53,0.73,0.8);
            		rgb(58.64286150251116bp)=(0.05,0.17,0.22);
            		rgb(100bp)=(0.05,0.17,0.22)}
            	\tikzset {_z4she489p/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-98 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_4gscxo6fz}{150bp}{rgb(0bp)=(0.5,0.59,0.62);
            		rgb(37.5bp)=(0.5,0.59,0.62);
            		rgb(45.0357164655413bp)=(1,1,1);
            		rgb(51.875bp)=(0.53,0.73,0.8);
            		rgb(58.64286150251116bp)=(0.05,0.17,0.22);
            		rgb(100bp)=(0.05,0.17,0.22)}
            	\tikzset {_irxstjkr9/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-98 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_0kpz9vs28}{150bp}{rgb(0bp)=(0.5,0.59,0.62);
            		rgb(37.5bp)=(0.5,0.59,0.62);
            		rgb(45.0357164655413bp)=(1,1,1);
            		rgb(51.875bp)=(0.53,0.73,0.8);
            		rgb(58.64286150251116bp)=(0.05,0.17,0.22);
            		rgb(100bp)=(0.05,0.17,0.22)}
            	\tikzset {_727n6dqui/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-98 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_udalafu2k}{150bp}{rgb(0bp)=(0.5,0.59,0.62);
            		rgb(37.5bp)=(0.5,0.59,0.62);
            		rgb(45.0357164655413bp)=(1,1,1);
            		rgb(51.875bp)=(0.53,0.73,0.8);
            		rgb(58.64286150251116bp)=(0.05,0.17,0.22);
            		rgb(100bp)=(0.05,0.17,0.22)}
            	\tikzset {_59ki5mhnp/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-98 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_7bkvlzuhm}{150bp}{rgb(0bp)=(0.5,0.59,0.62);
            		rgb(37.5bp)=(0.5,0.59,0.62);
            		rgb(45.0357164655413bp)=(1,1,1);
            		rgb(51.875bp)=(0.53,0.73,0.8);
            		rgb(58.64286150251116bp)=(0.05,0.17,0.22);
            		rgb(100bp)=(0.05,0.17,0.22)}
            	\tikzset {_7xhvfdx4v/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-98 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_sgy97e4fj}{150bp}{rgb(0bp)=(0.5,0.59,0.62);
            		rgb(37.5bp)=(0.5,0.59,0.62);
            		rgb(45.0357164655413bp)=(1,1,1);
            		rgb(51.875bp)=(0.53,0.73,0.8);
            		rgb(58.64286150251116bp)=(0.05,0.17,0.22);
            		rgb(100bp)=(0.05,0.17,0.22)}
            	\tikzset {_abvw1j4of/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-98 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_gai4vhgny}{150bp}{rgb(0bp)=(0.5,0.59,0.62);
            		rgb(37.5bp)=(0.5,0.59,0.62);
            		rgb(45.0357164655413bp)=(1,1,1);
            		rgb(51.875bp)=(0.53,0.73,0.8);
            		rgb(58.64286150251116bp)=(0.05,0.17,0.22);
            		rgb(100bp)=(0.05,0.17,0.22)}
            	\tikzset {_cjlleiya0/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{35.67 bp } { 0 bp }  }  \pgftransformscale{2.46 }  }}}
            	\pgfdeclareradialshading{_e9t57o95v}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(0.02,0.11,0.12);
            		rgb(0bp)=(0.02,0.11,0.12);
            		rgb(25bp)=(0.43,0.63,0.67);
            		rgb(400bp)=(0.43,0.63,0.67)}
            	\tikzset {_d55jkmkyl/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{35.67 bp } { 0 bp }  }  \pgftransformscale{2.46 }  }}}
            	\pgfdeclareradialshading{_rltpkyhvo}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(0.02,0.11,0.12);
            		rgb(0bp)=(0.02,0.11,0.12);
            		rgb(25bp)=(0.43,0.63,0.67);
            		rgb(400bp)=(0.43,0.63,0.67)}
            	\tikzset {_qjjcxlaef/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{35.67 bp } { 0 bp }  }  \pgftransformscale{2.46 }  }}}
            	\pgfdeclareradialshading{_gtytvvrva}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(0.02,0.11,0.12);
            		rgb(0bp)=(0.02,0.11,0.12);
            		rgb(25bp)=(0.43,0.63,0.67);
            		rgb(400bp)=(0.43,0.63,0.67)}
            	\tikzset {_qljbju607/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{35.67 bp } { 0 bp }  }  \pgftransformscale{2.46 }  }}}
            	\pgfdeclareradialshading{_kuupj2yv3}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(0.02,0.11,0.12);
            		rgb(0bp)=(0.02,0.11,0.12);
            		rgb(25bp)=(0.43,0.63,0.67);
            		rgb(400bp)=(0.43,0.63,0.67)}
            	\tikzset {_p4tx8j7rn/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{35.67 bp } { 0 bp }  }  \pgftransformscale{2.46 }  }}}
            	\pgfdeclareradialshading{_byezy238e}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(0.02,0.11,0.12);
            		rgb(0bp)=(0.02,0.11,0.12);
            		rgb(25bp)=(0.43,0.63,0.67);
            		rgb(400bp)=(0.43,0.63,0.67)}
            	\tikzset{every picture/.style={line width=0.75pt}}      
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.3 ] (409.51,153.45) -- (251.15,188.59) -- (126.01,133.08) -- (101.6,119.34) -- (254.92,111.4) -- cycle ;
            	\path  [shading=_pukzoevxm,_1cq8tbgdl] (258.03,96.57) .. controls (266.71,96.16) and (267.6,106.62) .. (262.1,110.08) .. controls (200.75,117.61) and (181.85,119.57) .. (124.06,126.14) .. controls (114.85,110.07) and (132.78,116.82) .. (123.58,103.64) .. controls (162.1,102.38) and (240.88,96.93) .. (258.03,96.57) -- cycle ; 
            	\draw   (258.03,96.57) .. controls (266.71,96.16) and (267.6,106.62) .. (262.1,110.08) .. controls (200.75,117.61) and (181.85,119.57) .. (124.06,126.14) .. controls (114.85,110.07) and (132.78,116.82) .. (123.58,103.64) .. controls (162.1,102.38) and (240.88,96.93) .. (258.03,96.57) -- cycle ; 
            	\draw  [fill={rgb, 255:red, 125; green, 168; blue, 177 }  ,fill opacity=1 ] (114.03,115.1) .. controls (113.9,108.88) and (118.18,103.76) .. (123.58,103.64) .. controls (128.99,103.53) and (133.48,108.47) .. (133.61,114.68) .. controls (133.74,120.9) and (129.47,126.03) .. (124.06,126.14) .. controls (118.65,126.25) and (114.16,121.31) .. (114.03,115.1) -- cycle ;
            	\path  [shading=_ti4umxxhc,_nnivuyq7h] (116.93,115.04) .. controls (116.83,110.42) and (119.84,106.62) .. (123.65,106.54) .. controls (127.45,106.46) and (130.62,110.13) .. (130.72,114.75) .. controls (130.81,119.36) and (127.81,123.16) .. (124,123.24) .. controls (120.19,123.32) and (117.03,119.65) .. (116.93,115.04) -- cycle ; 
            	\draw   (116.93,115.04) .. controls (116.83,110.42) and (119.84,106.62) .. (123.65,106.54) .. controls (127.45,106.46) and (130.62,110.13) .. (130.72,114.75) .. controls (130.81,119.36) and (127.81,123.16) .. (124,123.24) .. controls (120.19,123.32) and (117.03,119.65) .. (116.93,115.04) -- cycle ; 
            	\path  [shading=_jxbo9xttp,_8gsqgqc2b] (276.87,105.91) .. controls (285.55,105.5) and (286.44,115.96) .. (280.95,119.41) .. controls (219.6,126.95) and (200.7,128.91) .. (142.9,135.48) .. controls (133.69,119.4) and (151.62,126.16) .. (142.43,112.98) .. controls (180.94,111.72) and (259.72,106.27) .. (276.87,105.91) -- cycle ; 
            	\draw   (276.87,105.91) .. controls (285.55,105.5) and (286.44,115.96) .. (280.95,119.41) .. controls (219.6,126.95) and (200.7,128.91) .. (142.9,135.48) .. controls (133.69,119.4) and (151.62,126.16) .. (142.43,112.98) .. controls (180.94,111.72) and (259.72,106.27) .. (276.87,105.91) -- cycle ; 
            	\draw  [fill={rgb, 255:red, 125; green, 168; blue, 177 }  ,fill opacity=1 ] (132.87,124.44) .. controls (132.74,118.22) and (137.02,113.09) .. (142.43,112.98) .. controls (147.83,112.87) and (152.32,117.81) .. (152.46,124.02) .. controls (152.59,130.24) and (148.31,135.36) .. (142.9,135.48) .. controls (137.5,135.59) and (133.01,130.65) .. (132.87,124.44) -- cycle ;
            	\path  [shading=_un8983qdx,_ga1bjgsz2] (135.77,124.37) .. controls (135.67,119.76) and (138.68,115.96) .. (142.49,115.88) .. controls (146.3,115.8) and (149.46,119.47) .. (149.56,124.08) .. controls (149.66,128.7) and (146.65,132.5) .. (142.84,132.58) .. controls (139.03,132.66) and (135.87,128.99) .. (135.77,124.37) -- cycle ;
            	\draw   (135.77,124.37) .. controls (135.67,119.76) and (138.68,115.96) .. (142.49,115.88) .. controls (146.3,115.8) and (149.46,119.47) .. (149.56,124.08) .. controls (149.66,128.7) and (146.65,132.5) .. (142.84,132.58) .. controls (139.03,132.66) and (135.87,128.99) .. (135.77,124.37) -- cycle ; 
            	\path  [shading=_rwyc1mvtc,_zadpmdwqh] (295.68,114.25) .. controls (304.36,113.84) and (305.25,124.29) .. (299.75,127.75) .. controls (238.4,135.29) and (219.5,137.25) .. (161.71,143.82) .. controls (152.5,127.74) and (170.43,134.5) .. (161.23,121.32) .. controls (199.75,120.06) and (278.53,114.61) .. (295.68,114.25) -- cycle ; 
            	\draw   (295.68,114.25) .. controls (304.36,113.84) and (305.25,124.29) .. (299.75,127.75) .. controls (238.4,135.29) and (219.5,137.25) .. (161.71,143.82) .. controls (152.5,127.74) and (170.43,134.5) .. (161.23,121.32) .. controls (199.75,120.06) and (278.53,114.61) .. (295.68,114.25) -- cycle ; 
            	\draw  [fill={rgb, 255:red, 125; green, 168; blue, 177 }  ,fill opacity=1 ] (151.68,132.77) .. controls (151.55,126.56) and (155.83,121.43) .. (161.23,121.32) .. controls (166.64,121.2) and (171.13,126.15) .. (171.26,132.36) .. controls (171.39,138.57) and (167.12,143.7) .. (161.71,143.82) .. controls (156.3,143.93) and (151.81,138.99) .. (151.68,132.77) -- cycle ;
            	\path  [shading=_c9hs7isav,_srv4fh1ip] (154.58,132.71) .. controls (154.48,128.1) and (157.49,124.3) .. (161.3,124.21) .. controls (165.1,124.13) and (168.27,127.81) .. (168.37,132.42) .. controls (168.46,137.04) and (165.46,140.84) .. (161.65,140.92) .. controls (157.84,141) and (154.68,137.33) .. (154.58,132.71) -- cycle ;  
            	\draw   (154.58,132.71) .. controls (154.48,128.1) and (157.49,124.3) .. (161.3,124.21) .. controls (165.1,124.13) and (168.27,127.81) .. (168.37,132.42) .. controls (168.46,137.04) and (165.46,140.84) .. (161.65,140.92) .. controls (157.84,141) and (154.68,137.33) .. (154.58,132.71) -- cycle ; 
            	\path  [shading=_26kcivj3b,_h5riw555j] (316,123.03) .. controls (324.69,122.62) and (325.57,133.08) .. (320.08,136.54) .. controls (258.73,144.07) and (239.83,146.03) .. (182.03,152.6) .. controls (172.82,136.53) and (190.75,143.28) .. (181.56,130.1) .. controls (220.08,128.85) and (298.85,123.39) .. (316,123.03) -- cycle ; 
            	\draw   (316,123.03) .. controls (324.69,122.62) and (325.57,133.08) .. (320.08,136.54) .. controls (258.73,144.07) and (239.83,146.03) .. (182.03,152.6) .. controls (172.82,136.53) and (190.75,143.28) .. (181.56,130.1) .. controls (220.08,128.85) and (298.85,123.39) .. (316,123.03) -- cycle ; 
            	\draw  [fill={rgb, 255:red, 125; green, 168; blue, 177 }  ,fill opacity=1 ] (172.01,141.56) .. controls (171.87,135.35) and (176.15,130.22) .. (181.56,130.1) .. controls (186.97,129.99) and (191.46,134.93) .. (191.59,141.15) .. controls (191.72,147.36) and (187.44,152.49) .. (182.03,152.6) .. controls (176.63,152.72) and (172.14,147.77) .. (172.01,141.56) -- cycle ;
            	\path  [shading=_w5o9wo1r0,_9mix4x0rz] (174.9,141.5) .. controls (174.8,136.89) and (177.81,133.08) .. (181.62,133) .. controls (185.43,132.92) and (188.59,136.59) .. (188.69,141.21) .. controls (188.79,145.82) and (185.78,149.63) .. (181.97,149.71) .. controls (178.17,149.79) and (175,146.11) .. (174.9,141.5) -- cycle ; 
            	\draw   (174.9,141.5) .. controls (174.8,136.89) and (177.81,133.08) .. (181.62,133) .. controls (185.43,132.92) and (188.59,136.59) .. (188.69,141.21) .. controls (188.79,145.82) and (185.78,149.63) .. (181.97,149.71) .. controls (178.17,149.79) and (175,146.11) .. (174.9,141.5) -- cycle ; 
            	\path  [shading=_tt0bwwccr,_a47ywyjip] (334.83,131.87) .. controls (343.51,131.46) and (344.4,141.92) .. (338.9,145.38) .. controls (277.55,152.91) and (258.65,154.87) .. (200.86,161.44) .. controls (191.65,145.37) and (209.58,152.12) .. (200.38,138.94) .. controls (238.9,137.68) and (317.68,132.23) .. (334.83,131.87) -- cycle ; 
            	\draw   (334.83,131.87) .. controls (343.51,131.46) and (344.4,141.92) .. (338.9,145.38) .. controls (277.55,152.91) and (258.65,154.87) .. (200.86,161.44) .. controls (191.65,145.37) and (209.58,152.12) .. (200.38,138.94) .. controls (238.9,137.68) and (317.68,132.23) .. (334.83,131.87) -- cycle ; 
            	\draw  [fill={rgb, 255:red, 125; green, 168; blue, 177 }  ,fill opacity=1 ] (190.83,150.4) .. controls (190.7,144.19) and (194.98,139.06) .. (200.38,138.94) .. controls (205.79,138.83) and (210.28,143.77) .. (210.41,149.99) .. controls (210.54,156.2) and (206.27,161.33) .. (200.86,161.44) .. controls (195.45,161.56) and (190.96,156.61) .. (190.83,150.4) -- cycle ;
            	\path  [shading=_yt0ahcbye,_9p6uo6sx7] (193.73,150.34) .. controls (193.63,145.72) and (196.64,141.92) .. (200.44,141.84) .. controls (204.25,141.76) and (207.42,145.43) .. (207.52,150.05) .. controls (207.61,154.66) and (204.61,158.47) .. (200.8,158.55) .. controls (196.99,158.63) and (193.82,154.95) .. (193.73,150.34) -- cycle ; 
            	\draw   (193.73,150.34) .. controls (193.63,145.72) and (196.64,141.92) .. (200.44,141.84) .. controls (204.25,141.76) and (207.42,145.43) .. (207.52,150.05) .. controls (207.61,154.66) and (204.61,158.47) .. (200.8,158.55) .. controls (196.99,158.63) and (193.82,154.95) .. (193.73,150.34) -- cycle ; 
            	\path  [shading=_77zkno9r5,_c8jrgvosu] (354.15,140.69) .. controls (362.83,140.28) and (363.72,150.74) .. (358.23,154.2) .. controls (296.88,161.73) and (277.98,163.69) .. (220.18,170.26) .. controls (210.97,154.19) and (228.9,160.94) .. (219.71,147.76) .. controls (258.22,146.51) and (337,141.05) .. (354.15,140.69) -- cycle ;  
            	\draw   (354.15,140.69) .. controls (362.83,140.28) and (363.72,150.74) .. (358.23,154.2) .. controls (296.88,161.73) and (277.98,163.69) .. (220.18,170.26) .. controls (210.97,154.19) and (228.9,160.94) .. (219.71,147.76) .. controls (258.22,146.51) and (337,141.05) .. (354.15,140.69) -- cycle ; 
            	\draw  [fill={rgb, 255:red, 125; green, 168; blue, 177 }  ,fill opacity=1 ] (210.16,159.22) .. controls (210.02,153.01) and (214.3,147.88) .. (219.71,147.76) .. controls (225.12,147.65) and (229.6,152.59) .. (229.74,158.81) .. controls (229.87,165.02) and (225.59,170.15) .. (220.18,170.26) .. controls (214.78,170.38) and (210.29,165.43) .. (210.16,159.22) -- cycle ;
            	\path  [shading=_jhj98xcb8,_hu48qnyiy] (213.05,159.16) .. controls (212.95,154.55) and (215.96,150.74) .. (219.77,150.66) .. controls (223.58,150.58) and (226.74,154.25) .. (226.84,158.87) .. controls (226.94,163.48) and (223.93,167.29) .. (220.12,167.37) .. controls (216.31,167.45) and (213.15,163.77) .. (213.05,159.16) -- cycle ; 
            	\draw   (213.05,159.16) .. controls (212.95,154.55) and (215.96,150.74) .. (219.77,150.66) .. controls (223.58,150.58) and (226.74,154.25) .. (226.84,158.87) .. controls (226.94,163.48) and (223.93,167.29) .. (220.12,167.37) .. controls (216.31,167.45) and (213.15,163.77) .. (213.05,159.16) -- cycle ; 
            	\path  [shading=_58wrmdubh,_rp8ouo667] (275.25,89.36) .. controls (283.94,89.32) and (284.39,99.81) .. (278.75,103.03) .. controls (217.13,107.97) and (198.17,109.13) .. (140.15,113.25) .. controls (131.63,96.8) and (149.25,104.31) .. (140.62,90.75) .. controls (179.16,91.12) and (258.09,89) .. (275.25,89.36) -- cycle ;  
            	\draw   (275.25,89.36) .. controls (283.94,89.32) and (284.39,99.81) .. (278.75,103.03) .. controls (217.13,107.97) and (198.17,109.13) .. (140.15,113.25) .. controls (131.63,96.8) and (149.25,104.31) .. (140.62,90.75) .. controls (179.16,91.12) and (258.09,89) .. (275.25,89.36) -- cycle ; 
            	\draw  [fill={rgb, 255:red, 125; green, 168; blue, 177 }  ,fill opacity=1 ] (130.6,101.8) .. controls (130.73,95.58) and (135.22,90.64) .. (140.62,90.75) .. controls (146.03,90.87) and (150.31,96) .. (150.18,102.21) .. controls (150.04,108.42) and (145.56,113.37) .. (140.15,113.25) .. controls (134.74,113.14) and (130.46,108.01) .. (130.6,101.8) -- cycle ;
            	\path  [shading=_pbfywygmd,_9hxnzzlhk] (133.49,101.86) .. controls (133.59,97.24) and (136.75,93.57) .. (140.56,93.65) .. controls (144.37,93.73) and (147.38,97.54) .. (147.28,102.15) .. controls (147.18,106.76) and (144.02,110.44) .. (140.21,110.36) .. controls (136.4,110.28) and (133.39,106.47) .. (133.49,101.86) -- cycle ; 
            	\draw   (133.49,101.86) .. controls (133.59,97.24) and (136.75,93.57) .. (140.56,93.65) .. controls (144.37,93.73) and (147.38,97.54) .. (147.28,102.15) .. controls (147.18,106.76) and (144.02,110.44) .. (140.21,110.36) .. controls (136.4,110.28) and (133.39,106.47) .. (133.49,101.86) -- cycle ; 
            	\path  [shading=_8juxqe6jq,_or93c5u4y] (295.34,100.22) .. controls (304.03,100.37) and (304.24,110.87) .. (298.53,113.96) .. controls (236.82,117.51) and (217.83,118.24) .. (159.74,121.06) .. controls (151.59,104.42) and (169.04,112.32) .. (160.72,98.58) .. controls (199.24,99.81) and (278.2,99.47) .. (295.34,100.22) -- cycle ; 
            	\draw   (295.34,100.22) .. controls (304.03,100.37) and (304.24,110.87) .. (298.53,113.96) .. controls (236.82,117.51) and (217.83,118.24) .. (159.74,121.06) .. controls (151.59,104.42) and (169.04,112.32) .. (160.72,98.58) .. controls (199.24,99.81) and (278.2,99.47) .. (295.34,100.22) -- cycle ; 
            	\draw  [fill={rgb, 255:red, 125; green, 168; blue, 177 }  ,fill opacity=1 ] (150.45,109.39) .. controls (150.72,103.18) and (155.32,98.34) .. (160.72,98.58) .. controls (166.12,98.81) and (170.28,104.04) .. (170.01,110.25) .. controls (169.74,116.45) and (165.14,121.3) .. (159.74,121.06) .. controls (154.33,120.82) and (150.17,115.6) .. (150.45,109.39) -- cycle ;
            	\path  [shading=_2bxmlrjnt,_i3q09xmt6] (153.34,109.52) .. controls (153.54,104.91) and (156.79,101.31) .. (160.59,101.47) .. controls (164.4,101.64) and (167.32,105.51) .. (167.12,110.12) .. controls (166.92,114.73) and (163.67,118.33) .. (159.86,118.17) .. controls (156.06,118) and (153.14,114.13) .. (153.34,109.52) -- cycle ; 
            	\draw   (153.34,109.52) .. controls (153.54,104.91) and (156.79,101.31) .. (160.59,101.47) .. controls (164.4,101.64) and (167.32,105.51) .. (167.12,110.12) .. controls (166.92,114.73) and (163.67,118.33) .. (159.86,118.17) .. controls (156.06,118) and (153.14,114.13) .. (153.34,109.52) -- cycle ; 
            	\path  [shading=_w4luiv4xm,_54rjonueu] (314.66,109.04) .. controls (323.35,109.2) and (323.57,119.69) .. (317.85,122.78) .. controls (256.15,126.33) and (237.16,127.06) .. (179.06,129.88) .. controls (170.91,113.24) and (188.36,121.14) .. (180.04,107.4) .. controls (218.56,108.63) and (297.52,108.29) .. (314.66,109.04) -- cycle ; 
            	\draw   (314.66,109.04) .. controls (323.35,109.2) and (323.57,119.69) .. (317.85,122.78) .. controls (256.15,126.33) and (237.16,127.06) .. (179.06,129.88) .. controls (170.91,113.24) and (188.36,121.14) .. (180.04,107.4) .. controls (218.56,108.63) and (297.52,108.29) .. (314.66,109.04) -- cycle ; 
            	\draw  [fill={rgb, 255:red, 125; green, 168; blue, 177 }  ,fill opacity=1 ] (169.77,118.21) .. controls (170.04,112) and (174.64,107.16) .. (180.04,107.4) .. controls (185.45,107.63) and (189.61,112.86) .. (189.34,119.07) .. controls (189.07,125.28) and (184.47,130.12) .. (179.06,129.88) .. controls (173.66,129.64) and (169.5,124.42) .. (169.77,118.21) -- cycle ;
            	\path  [shading=_kp21bct93,_og9wjhs94] (172.66,118.34) .. controls (172.86,113.73) and (176.11,110.13) .. (179.92,110.29) .. controls (183.72,110.46) and (186.64,114.33) .. (186.44,118.94) .. controls (186.24,123.55) and (182.99,127.15) .. (179.19,126.99) .. controls (175.38,126.82) and (172.46,122.95) .. (172.66,118.34) -- cycle ; 
            	\draw   (172.66,118.34) .. controls (172.86,113.73) and (176.11,110.13) .. (179.92,110.29) .. controls (183.72,110.46) and (186.64,114.33) .. (186.44,118.94) .. controls (186.24,123.55) and (182.99,127.15) .. (179.19,126.99) .. controls (175.38,126.82) and (172.46,122.95) .. (172.66,118.34) -- cycle ; 
            	\path  [shading=_zlb1kxgtb,_6fufbomtd] (333.45,116.88) .. controls (342.14,117.03) and (342.35,127.53) .. (336.64,130.62) .. controls (274.94,134.17) and (255.95,134.9) .. (197.85,137.72) .. controls (189.7,121.08) and (207.15,128.98) .. (198.83,115.24) .. controls (237.35,116.47) and (316.31,116.13) .. (333.45,116.88) -- cycle ; 
            	\draw   (333.45,116.88) .. controls (342.14,117.03) and (342.35,127.53) .. (336.64,130.62) .. controls (274.94,134.17) and (255.95,134.9) .. (197.85,137.72) .. controls (189.7,121.08) and (207.15,128.98) .. (198.83,115.24) .. controls (237.35,116.47) and (316.31,116.13) .. (333.45,116.88) -- cycle ;
            	\draw  [fill={rgb, 255:red, 125; green, 168; blue, 177 }  ,fill opacity=1 ] (188.56,126.05) .. controls (188.83,119.84) and (193.43,115) .. (198.83,115.24) .. controls (204.24,115.47) and (208.4,120.7) .. (208.13,126.91) .. controls (207.85,133.11) and (203.25,137.96) .. (197.85,137.72) .. controls (192.45,137.48) and (188.29,132.26) .. (188.56,126.05) -- cycle ;
            	\path  [shading=_3vg7tiuuo,_mvftxkv8i] (191.45,126.18) .. controls (191.65,121.57) and (194.9,117.97) .. (198.71,118.13) .. controls (202.51,118.3) and (205.43,122.17) .. (205.23,126.78) .. controls (205.03,131.39) and (201.78,134.99) .. (197.98,134.83) .. controls (194.17,134.66) and (191.25,130.79) .. (191.45,126.18) -- cycle ; 
            	\draw   (191.45,126.18) .. controls (191.65,121.57) and (194.9,117.97) .. (198.71,118.13) .. controls (202.51,118.3) and (205.43,122.17) .. (205.23,126.78) .. controls (205.03,131.39) and (201.78,134.99) .. (197.98,134.83) .. controls (194.17,134.66) and (191.25,130.79) .. (191.45,126.18) -- cycle ; 
            	\path  [shading=_ulms6jrnz,_g1rg47fai] (351.85,127.73) .. controls (360.54,127.89) and (360.75,138.38) .. (355.04,141.48) .. controls (293.33,145.03) and (274.34,145.76) .. (216.25,148.58) .. controls (208.1,131.94) and (225.55,139.84) .. (217.23,126.09) .. controls (255.75,127.33) and (334.71,126.99) .. (351.85,127.73) -- cycle ; 
            	\draw   (351.85,127.73) .. controls (360.54,127.89) and (360.75,138.38) .. (355.04,141.48) .. controls (293.33,145.03) and (274.34,145.76) .. (216.25,148.58) .. controls (208.1,131.94) and (225.55,139.84) .. (217.23,126.09) .. controls (255.75,127.33) and (334.71,126.99) .. (351.85,127.73) -- cycle ; 
            	\path  [shading=_zflny2v34,_j9godp156] (206.96,136.91) .. controls (207.23,130.7) and (211.83,125.86) .. (217.23,126.09) .. controls (222.63,126.33) and (226.79,131.55) .. (226.52,137.76) .. controls (226.25,143.97) and (221.65,148.81) .. (216.25,148.58) .. controls (210.84,148.34) and (206.68,143.12) .. (206.96,136.91) -- cycle ; 
            	\draw   (206.96,136.91) .. controls (207.23,130.7) and (211.83,125.86) .. (217.23,126.09) .. controls (222.63,126.33) and (226.79,131.55) .. (226.52,137.76) .. controls (226.25,143.97) and (221.65,148.81) .. (216.25,148.58) .. controls (210.84,148.34) and (206.68,143.12) .. (206.96,136.91) -- cycle ; 
            	\path  [shading=_x9fgrw5gw,_l8v4o66f7] (295.11,84.8) .. controls (303.78,85.4) and (303.45,95.89) .. (297.59,98.68) .. controls (235.78,99.05) and (216.78,98.81) .. (158.61,98.63) .. controls (151.33,81.6) and (168.35,90.38) .. (160.75,76.23) .. controls (199.15,79.45) and (278.03,83.17) .. (295.11,84.8) -- cycle ; 
            	\draw   (295.11,84.8) .. controls (303.78,85.4) and (303.45,95.89) .. (297.59,98.68) .. controls (235.78,99.05) and (216.78,98.81) .. (158.61,98.63) .. controls (151.33,81.6) and (168.35,90.38) .. (160.75,76.23) .. controls (199.15,79.45) and (278.03,83.17) .. (295.11,84.8) -- cycle ; 
            	\path  [shading=_e0mv7ftih,_he7v6m6cf] (149.93,86.5) .. controls (150.52,80.31) and (155.37,75.72) .. (160.75,76.23) .. controls (166.13,76.74) and (170.02,82.17) .. (169.43,88.36) .. controls (168.84,94.55) and (164,99.14) .. (158.61,98.63) .. controls (153.23,98.12) and (149.34,92.69) .. (149.93,86.5) -- cycle ; 
            	\draw   (149.93,86.5) .. controls (150.52,80.31) and (155.37,75.72) .. (160.75,76.23) .. controls (166.13,76.74) and (170.02,82.17) .. (169.43,88.36) .. controls (168.84,94.55) and (164,99.14) .. (158.61,98.63) .. controls (153.23,98.12) and (149.34,92.69) .. (149.93,86.5) -- cycle ; 
            	\path  [shading=_4gscxo6fz,_z4she489p] (314.93,93.6) .. controls (323.6,94.2) and (323.27,104.69) .. (317.41,107.49) .. controls (255.6,107.86) and (236.6,107.61) .. (178.44,107.43) .. controls (171.16,90.4) and (188.18,99.19) .. (180.58,85.03) .. controls (218.98,88.25) and (297.85,91.97) .. (314.93,93.6) -- cycle ; 
            	\draw   (314.93,93.6) .. controls (323.6,94.2) and (323.27,104.69) .. (317.41,107.49) .. controls (255.6,107.86) and (236.6,107.61) .. (178.44,107.43) .. controls (171.16,90.4) and (188.18,99.19) .. (180.58,85.03) .. controls (218.98,88.25) and (297.85,91.97) .. (314.93,93.6) -- cycle ; 
            	\path  [shading=_0kpz9vs28,_irxstjkr9] (169.76,95.3) .. controls (170.35,89.12) and (175.19,84.52) .. (180.58,85.03) .. controls (185.96,85.55) and (189.84,90.98) .. (189.25,97.16) .. controls (188.66,103.35) and (183.82,107.95) .. (178.44,107.43) .. controls (173.05,106.92) and (169.17,101.49) .. (169.76,95.3) -- cycle ; 
            	\draw   (169.76,95.3) .. controls (170.35,89.12) and (175.19,84.52) .. (180.58,85.03) .. controls (185.96,85.55) and (189.84,90.98) .. (189.25,97.16) .. controls (188.66,103.35) and (183.82,107.95) .. (178.44,107.43) .. controls (173.05,106.92) and (169.17,101.49) .. (169.76,95.3) -- cycle ; 
            	\path  [shading=_udalafu2k,_727n6dqui] (332.69,100.47) .. controls (341.36,101.08) and (341.03,111.57) .. (335.17,114.36) .. controls (273.36,114.73) and (254.36,114.49) .. (196.19,114.31) .. controls (188.91,97.28) and (205.93,106.06) .. (198.33,91.91) .. controls (236.73,95.12) and (315.61,98.84) .. (332.69,100.47) -- cycle ;  
            	\draw   (332.69,100.47) .. controls (341.36,101.08) and (341.03,111.57) .. (335.17,114.36) .. controls (273.36,114.73) and (254.36,114.49) .. (196.19,114.31) .. controls (188.91,97.28) and (205.93,106.06) .. (198.33,91.91) .. controls (236.73,95.12) and (315.61,98.84) .. (332.69,100.47) -- cycle ; 
            	\path  [shading=_7bkvlzuhm,_59ki5mhnp] (187.51,102.18) .. controls (188.1,95.99) and (192.95,91.39) .. (198.33,91.91) .. controls (203.71,92.42) and (207.6,97.85) .. (207.01,104.04) .. controls (206.42,110.22) and (201.58,114.82) .. (196.19,114.31) .. controls (190.81,113.8) and (186.92,108.36) .. (187.51,102.18) -- cycle ; 
            	\draw   (187.51,102.18) .. controls (188.1,95.99) and (192.95,91.39) .. (198.33,91.91) .. controls (203.71,92.42) and (207.6,97.85) .. (207.01,104.04) .. controls (206.42,110.22) and (201.58,114.82) .. (196.19,114.31) .. controls (190.81,113.8) and (186.92,108.36) .. (187.51,102.18) -- cycle ; 
            	\path  [shading=_sgy97e4fj,_7xhvfdx4v] (351.1,111.83) .. controls (359.77,112.43) and (357.71,124.94) .. (351.85,127.73) .. controls (290.04,128.1) and (272.77,125.84) .. (214.61,125.66) .. controls (207.32,108.63) and (224.35,117.42) .. (216.74,103.26) .. controls (255.15,106.48) and (334.02,110.2) .. (351.1,111.83) -- cycle ; 
            	\draw   (351.1,111.83) .. controls (359.77,112.43) and (357.71,124.94) .. (351.85,127.73) .. controls (290.04,128.1) and (272.77,125.84) .. (214.61,125.66) .. controls (207.32,108.63) and (224.35,117.42) .. (216.74,103.26) .. controls (255.15,106.48) and (334.02,110.2) .. (351.1,111.83) -- cycle ; 
            	\path  [shading=_gai4vhgny,_abvw1j4of] (205.93,113.53) .. controls (206.52,107.35) and (211.36,102.75) .. (216.74,103.26) .. controls (222.13,103.78) and (226.01,109.21) .. (225.42,115.39) .. controls (224.83,121.58) and (219.99,126.18) .. (214.61,125.66) .. controls (209.22,125.15) and (205.34,119.72) .. (205.93,113.53) -- cycle ;  
            	\draw   (205.93,113.53) .. controls (206.52,107.35) and (211.36,102.75) .. (216.74,103.26) .. controls (222.13,103.78) and (226.01,109.21) .. (225.42,115.39) .. controls (224.83,121.58) and (219.99,126.18) .. (214.61,125.66) .. controls (209.22,125.15) and (205.34,119.72) .. (205.93,113.53) -- cycle ; 
            	\path  [shading=_e9t57o95v,_cjlleiya0] (209.84,137.48) .. controls (209.75,132.87) and (212.75,129.06) .. (216.56,128.98) .. controls (220.37,128.9) and (223.54,132.58) .. (223.63,137.19) .. controls (223.73,141.8) and (220.72,145.61) .. (216.91,145.69) .. controls (213.11,145.77) and (209.94,142.09) .. (209.84,137.48) -- cycle ;  
            	\draw   (209.84,137.48) .. controls (209.75,132.87) and (212.75,129.06) .. (216.56,128.98) .. controls (220.37,128.9) and (223.54,132.58) .. (223.63,137.19) .. controls (223.73,141.8) and (220.72,145.61) .. (216.91,145.69) .. controls (213.11,145.77) and (209.94,142.09) .. (209.84,137.48) -- cycle ; 
            	\path  [shading=_rltpkyhvo,_d55jkmkyl] (208.78,114.61) .. controls (208.68,110) and (211.69,106.19) .. (215.5,106.11) .. controls (219.31,106.03) and (222.47,109.7) .. (222.57,114.32) .. controls (222.67,118.93) and (219.66,122.74) .. (215.85,122.82) .. controls (212.04,122.9) and (208.88,119.22) .. (208.78,114.61) -- cycle ; 
            	\draw   (208.78,114.61) .. controls (208.68,110) and (211.69,106.19) .. (215.5,106.11) .. controls (219.31,106.03) and (222.47,109.7) .. (222.57,114.32) .. controls (222.67,118.93) and (219.66,122.74) .. (215.85,122.82) .. controls (212.04,122.9) and (208.88,119.22) .. (208.78,114.61) -- cycle ; 
            	\path  [shading=_gtytvvrva,_qjjcxlaef] (190.37,103.25) .. controls (190.27,98.64) and (193.28,94.84) .. (197.08,94.76) .. controls (200.89,94.67) and (204.06,98.35) .. (204.16,102.96) .. controls (204.25,107.58) and (201.25,111.38) .. (197.44,111.46) .. controls (193.63,111.54) and (190.46,107.87) .. (190.37,103.25) -- cycle ; 
            	\draw   (190.37,103.25) .. controls (190.27,98.64) and (193.28,94.84) .. (197.08,94.76) .. controls (200.89,94.67) and (204.06,98.35) .. (204.16,102.96) .. controls (204.25,107.58) and (201.25,111.38) .. (197.44,111.46) .. controls (193.63,111.54) and (190.46,107.87) .. (190.37,103.25) -- cycle ;
            	\path  [shading=_kuupj2yv3,_qljbju607] (172.61,96.38) .. controls (172.51,91.77) and (175.52,87.96) .. (179.33,87.88) .. controls (183.14,87.8) and (186.3,91.47) .. (186.4,96.09) .. controls (186.5,100.7) and (183.49,104.51) .. (179.68,104.59) .. controls (175.88,104.67) and (172.71,100.99) .. (172.61,96.38) -- cycle ; 
            	\draw   (172.61,96.38) .. controls (172.51,91.77) and (175.52,87.96) .. (179.33,87.88) .. controls (183.14,87.8) and (186.3,91.47) .. (186.4,96.09) .. controls (186.5,100.7) and (183.49,104.51) .. (179.68,104.59) .. controls (175.88,104.67) and (172.71,100.99) .. (172.61,96.38) -- cycle ; 
            	\path  [shading=_byezy238e,_p4tx8j7rn] (152.79,87.58) .. controls (152.69,82.96) and (155.7,79.16) .. (159.51,79.08) .. controls (163.31,79) and (166.48,82.67) .. (166.58,87.28) .. controls (166.67,91.9) and (163.67,95.7) .. (159.86,95.78) .. controls (156.05,95.86) and (152.89,92.19) .. (152.79,87.58) -- cycle ;  
            	\draw   (152.79,87.58) .. controls (152.69,82.96) and (155.7,79.16) .. (159.51,79.08) .. controls (163.31,79) and (166.48,82.67) .. (166.58,87.28) .. controls (166.67,91.9) and (163.67,95.7) .. (159.86,95.78) .. controls (156.05,95.86) and (152.89,92.19) .. (152.79,87.58) -- cycle ; 
            \end{tikzpicture}'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Một công ty xây dựng cần xếp các ống thép hình trụ thành một chồng trong kho. Hàng dưới cùng có $%s$ ống, hàng thứ hai có $%s$ ống, hàng thứ ba có $%s$ ống, ... Cứ như thế, mỗi hàng phía trên ít hơn hàng ngay phía dưới là $1$ ống và hàng trên cùng có $%s$ ống. Biết giá tiền nhập kho của mỗi ống thép là $%s$ đồng. Tổng số tiền công ty đó đã chi để nhập toàn bộ số ống thép trên là bao nhiêu? (kết quả làm tròn đến hàng đơn vị của triệu đồng).}{%s}'''
                                 % (latex(u1), latex(u1-1), latex(u1-2), latex(un), latex(gia_moi_ong),hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Số hàng ống thép là: \\\\
                             $n = %s - %s + 1 = %s$. \\\\
                             Tổng số ống thép là tổng của một cấp số cộng: \\\\
                             $S = \\frac{\\left(%s + %s\\right) \\cdot %s}{2} = %s$ (ống). \\\\
                             Tổng số tiền công ty đã chi là: \\\\
                             $%s \\cdot %s = %s$ (đồng). \\\\
                             Đổi ra đơn vị triệu đồng: \\\\
                             $%s$ đồng $= %s$ triệu đồng. \\\\
                             Làm tròn đến hàng đơn vị của triệu đồng, ta được kết quả là: \\\\
                             $%s$ triệu đồng.'''
                           % (latex(u1), latex(un), latex(n),
                              latex(u1), latex(un), latex(n), latex(tong_so_ong),
                              latex(tong_so_ong), latex(gia_moi_ong), latex(tong_tien),
                              latex(tong_tien), str(trieu_dong).replace('.', ','), latex(kq_lam_tron)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_lam_tron))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

