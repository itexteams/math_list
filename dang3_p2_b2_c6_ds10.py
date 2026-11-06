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


def bt_dang3_p2_b2_c6_ds10(self):
            # Khai báo biến
            x=symbols('x')
            a=2
            b=3
            bt=a*x+b
            # Nội dung câu hỏi
            noidungcauhoi = ('''\\immini{Trong một trò chơi, con ngựa của bạn Toàn đang đứng ở vị trí xuất phát (như hình vẽ). Luật chơi như sau: Để di chuyển con ngựa, bạn Toàn cần gieo một con xúc xắc có sáu mặt cân đối, đồng chất. Ởmỗi lượt chơi, bạn có tối đa ba lần gieo. Ở lần gieo thứ nhất, con ngựa di chuyển đến ô có số thứ tự bằng số tương ứng với số chấm gieo được của con xúc xắc. Từ những lần gieo sau, nếu tổng của số tương ứng với số chấm gieo được của con xúc xắc và số tương ứng ghi ở ô con ngựa đang đứng lớn hơn $6$ thì con ngựa sẽ đứng yên, còn nếu tổng này nhỏ hơn hoặc bằng $6$ thì con ngựa được di chuyển số ô bằng số chấm gieo được. Con ngựa này gọi là về đích nếu nó đến được ô số $6$. }
                            {\\definecolor{ubqqys}{rgb}{0.29411764705882354,0.,0.5098039215686274}
            \\definecolor{ccccff}{rgb}{0.8,0.8,1.}
            \\definecolor{zzwwff}{rgb}{0.6,0.4,1.}
            \\definecolor{wwqqzz}{rgb}{0.4,0.,0.6}
            \\scalebox{0.4}{ 
            \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
                \\clip(-1.3542561475370944,-0.050662438518103085) rectangle (7,14.4217492318464);
                \\fill[line width=2.pt,color=wwqqzz,fill=wwqqzz,fill opacity=1.0] (0.5,2.) -- (1.,3.) -- (1.5,2.) -- cycle;
                \\fill[line width=2.pt,color=wwqqzz,fill=wwqqzz,fill opacity=1.0] (3.,2.) -- (3.5,3.) -- (4.,2.) -- cycle;
                \\fill[line width=2.pt,color=zzwwff,fill=zzwwff,fill opacity=1.0] (0.5,4.) -- (0.,3.) -- (0.5,2.) -- (1.,3.) -- cycle;
                \\fill[line width=2.pt,color=zzwwff,fill=zzwwff,fill opacity=1.0] (4.,4.) -- (3.5,3.) -- (4.,2.) -- (4.5,3.) -- cycle;
                \\fill[line width=2.pt,color=ccccff,fill=ccccff,fill opacity=1.0] (0.5,4.) -- (1.,3.) -- (1.5,4.) -- cycle;
                \\fill[line width=2.pt,color=ccccff,fill=ccccff,fill opacity=1.0] (3.,4.) -- (4.,4.) -- (3.5,3.) -- cycle;
                \\fill[line width=2.pt,color=wwqqzz,fill=wwqqzz,fill opacity=1.0] (0.5,4.) -- (1.,5.) -- (1.5,4.) -- cycle;
                \\fill[line width=2.pt,color=wwqqzz,fill=wwqqzz,fill opacity=1.0] (3.,4.) -- (3.5,5.) -- (4.,4.) -- cycle;
                \\fill[line width=2.pt,color=zzwwff,fill=zzwwff,fill opacity=1.0] (0.5,6.) -- (0.,5.) -- (0.5,4.) -- (1.,5.) -- cycle;
                \\fill[line width=2.pt,color=zzwwff,fill=zzwwff,fill opacity=1.0] (4.,6.) -- (3.5,5.) -- (4.,4.) -- (4.5,5.) -- cycle;
                \\fill[line width=2.pt,color=ccccff,fill=ccccff,fill opacity=1.0] (0.5,6.) -- (1.,5.) -- (1.5,6.) -- cycle;
                \\fill[line width=2.pt,color=ccccff,fill=ccccff,fill opacity=1.0] (3.,6.) -- (4.,6.) -- (3.5,5.) -- cycle;
                \\fill[line width=2.pt,color=wwqqzz,fill=wwqqzz,fill opacity=1.0] (0.5,6.) -- (1.,7.) -- (1.5,6.) -- cycle;
                \\fill[line width=2.pt,color=wwqqzz,fill=wwqqzz,fill opacity=1.0] (3.,6.) -- (3.5,7.) -- (4.,6.) -- cycle;
                \\fill[line width=2.pt,color=zzwwff,fill=zzwwff,fill opacity=1.0] (0.5,8.) -- (0.,7.) -- (0.5,6.) -- (1.,7.) -- cycle;
                \\fill[line width=2.pt,color=zzwwff,fill=zzwwff,fill opacity=1.0] (4.,8.) -- (3.5,7.) -- (4.,6.) -- (4.5,7.) -- cycle;
                \\fill[line width=2.pt,color=ccccff,fill=ccccff,fill opacity=1.0] (0.5,8.) -- (1.,7.) -- (1.5,8.) -- cycle;
                \\fill[line width=2.pt,color=ccccff,fill=ccccff,fill opacity=1.0] (3.,8.) -- (4.,8.) -- (3.5,7.) -- cycle;
                \\fill[line width=2.pt,color=wwqqzz,fill=wwqqzz,fill opacity=1.0] (0.5,8.) -- (1.,9.) -- (1.5,8.) -- cycle;
                \\fill[line width=2.pt,color=wwqqzz,fill=wwqqzz,fill opacity=1.0] (3.,8.) -- (3.5,9.) -- (4.,8.) -- cycle;
                \\fill[line width=2.pt,color=zzwwff,fill=zzwwff,fill opacity=1.0] (0.5,10.) -- (0.,9.) -- (0.5,8.) -- (1.,9.) -- cycle;
                \\fill[line width=2.pt,color=zzwwff,fill=zzwwff,fill opacity=1.0] (4.,10.) -- (3.5,9.) -- (4.,8.) -- (4.5,9.) -- cycle;
                \\fill[line width=2.pt,color=ccccff,fill=ccccff,fill opacity=1.0] (0.5,10.) -- (1.,9.) -- (1.5,10.) -- cycle;
                \\fill[line width=2.pt,color=ccccff,fill=ccccff,fill opacity=1.0] (3.,10.) -- (4.,10.) -- (3.5,9.) -- cycle;
                \\fill[line width=2.pt,color=wwqqzz,fill=wwqqzz,fill opacity=1.0] (0.5,10.) -- (1.,11.) -- (1.5,10.) -- cycle;
                \\fill[line width=2.pt,color=wwqqzz,fill=wwqqzz,fill opacity=1.0] (3.,10.) -- (3.5,11.) -- (4.,10.) -- cycle;
                \\fill[line width=2.pt,color=zzwwff,fill=zzwwff,fill opacity=1.0] (0.5,12.) -- (0.,11.) -- (0.5,10.) -- (1.,11.) -- cycle;
                \\fill[line width=2.pt,color=zzwwff,fill=zzwwff,fill opacity=1.0] (4.,12.) -- (3.5,11.) -- (4.,10.) -- (4.5,11.) -- cycle;
                \\fill[line width=2.pt,color=ccccff,fill=ccccff,fill opacity=1.0] (0.5,12.) -- (1.,11.) -- (1.5,12.) -- cycle;
                \\fill[line width=2.pt,color=ccccff,fill=ccccff,fill opacity=1.0] (3.,12.) -- (4.,12.) -- (3.5,11.) -- cycle;
                \\fill[line width=2.pt,color=wwqqzz,fill=wwqqzz,fill opacity=1.0] (0.5,12.) -- (1.,13.) -- (1.5,12.) -- cycle;
                \\fill[line width=2.pt,color=wwqqzz,fill=wwqqzz,fill opacity=1.0] (3.,12.) -- (3.5,13.) -- (4.,12.) -- cycle;
                \\fill[line width=2.pt,color=zzwwff,fill=zzwwff,fill opacity=1.0] (0.5,14.) -- (0.,13.) -- (0.5,12.) -- (1.,13.) -- cycle;
                \\fill[line width=2.pt,color=zzwwff,fill=zzwwff,fill opacity=1.0] (4.,14.) -- (3.5,13.) -- (4.,12.) -- (4.5,13.) -- cycle;
                \\fill[line width=2.pt,color=ccccff,fill=ccccff,fill opacity=1.0] (0.5,14.) -- (1.,13.) -- (1.5,14.) -- cycle;
                \\fill[line width=2.pt,color=ccccff,fill=ccccff,fill opacity=1.0] (3.,14.) -- (4.,14.) -- (3.5,13.) -- cycle;
                \\draw [line width=2.pt,color=ubqqys,fill=ubqqys,fill opacity=1.0] (2.2,1.) circle (0.6cm);
                \\draw [line width=2.pt] (1.5,2.)-- (3.,2.);
                \\draw [line width=2.pt] (0.5,2.)-- (4.,2.);
                \\draw [line width=2.pt,color=wwqqzz] (0.5,2.)-- (1.,3.);
                \\draw [line width=2.pt,color=wwqqzz] (1.,3.)-- (1.5,2.);
                \\draw [line width=2.pt,color=wwqqzz] (1.5,2.)-- (0.5,2.);
                \\draw [line width=2.pt,color=wwqqzz] (3.,2.)-- (3.5,3.);
                \\draw [line width=2.pt,color=wwqqzz] (3.5,3.)-- (4.,2.);
                \\draw [line width=2.pt,color=wwqqzz] (4.,2.)-- (3.,2.);
                \\draw [line width=2.pt,color=zzwwff] (0.5,4.)-- (0.,3.);
                \\draw [line width=2.pt,color=zzwwff] (0.,3.)-- (0.5,2.);
                \\draw [line width=2.pt,color=zzwwff] (0.5,2.)-- (1.,3.);
                \\draw [line width=2.pt,color=zzwwff] (1.,3.)-- (0.5,4.);
                \\draw [line width=2.pt,color=zzwwff] (4.,4.)-- (3.5,3.);
                \\draw [line width=2.pt,color=zzwwff] (3.5,3.)-- (4.,2.);
                \\draw [line width=2.pt,color=zzwwff] (4.,2.)-- (4.5,3.);
                \\draw [line width=2.pt,color=zzwwff] (4.5,3.)-- (4.,4.);
                \\draw [line width=2.pt,color=ccccff] (0.5,4.)-- (1.,3.);
                \\draw [line width=2.pt,color=ccccff] (1.,3.)-- (1.5,4.);
                \\draw [line width=2.pt,color=ccccff] (1.5,4.)-- (0.5,4.);
                \\draw [line width=2.pt,color=ccccff] (3.,4.)-- (4.,4.);
                \\draw [line width=2.pt,color=ccccff] (4.,4.)-- (3.5,3.);
                \\draw [line width=2.pt,color=ccccff] (3.5,3.)-- (3.,4.);
                \\draw [line width=2.pt] (0.,3.)-- (0.5,4.);
                \\draw [line width=2.pt] (0.5,4.)-- (1.,3.);
                \\draw [line width=2.pt] (1.,3.)-- (0.5,2.);
                \\draw [line width=2.pt] (0.5,2.)-- (0.,3.);
                \\draw [line width=2.pt] (1.,3.)-- (1.5,4.);
                \\draw [line width=2.pt] (1.,3.)-- (1.5,2.);
                \\draw [line width=2.pt] (1.5,4.)-- (3.,4.);
                \\draw [line width=2.pt] (3.,4.)-- (3.5,3.);
                \\draw [line width=2.pt] (3.5,3.)-- (3.,2.);
                \\draw [line width=2.pt] (3.,2.)-- (1.5,2.);
                \\draw [line width=2.pt] (3.5,3.)-- (4.,4.);
                \\draw [line width=2.pt] (4.,4.)-- (4.5,3.);
                \\draw [line width=2.pt] (4.5,3.)-- (4.,2.);
                \\draw [line width=2.pt] (4.,2.)-- (3.5,3.);
                \\draw [line width=2.pt] (0.5,4.)-- (4.,4.);
                \\draw [line width=2.pt] (0.5,2.)-- (4.,2.);
                \\draw [line width=2.pt,color=wwqqzz] (0.5,4.)-- (1.,5.);
                \\draw [line width=2.pt,color=wwqqzz] (1.,5.)-- (1.5,4.);
                \\draw [line width=2.pt,color=wwqqzz] (1.5,4.)-- (0.5,4.);
                \\draw [line width=2.pt,color=wwqqzz] (3.,4.)-- (3.5,5.);
                \\draw [line width=2.pt,color=wwqqzz] (3.5,5.)-- (4.,4.);
                \\draw [line width=2.pt,color=wwqqzz] (4.,4.)-- (3.,4.);
                \\draw [line width=2.pt,color=zzwwff] (0.5,6.)-- (0.,5.);
                \\draw [line width=2.pt,color=zzwwff] (0.,5.)-- (0.5,4.);
                \\draw [line width=2.pt,color=zzwwff] (0.5,4.)-- (1.,5.);
                \\draw [line width=2.pt,color=zzwwff] (1.,5.)-- (0.5,6.);
                \\draw [line width=2.pt,color=zzwwff] (4.,6.)-- (3.5,5.);
                \\draw [line width=2.pt,color=zzwwff] (3.5,5.)-- (4.,4.);
                \\draw [line width=2.pt,color=zzwwff] (4.,4.)-- (4.5,5.);
                \\draw [line width=2.pt,color=zzwwff] (4.5,5.)-- (4.,6.);
                \\draw [line width=2.pt,color=ccccff] (0.5,6.)-- (1.,5.);
                \\draw [line width=2.pt,color=ccccff] (1.,5.)-- (1.5,6.);
                \\draw [line width=2.pt,color=ccccff] (1.5,6.)-- (0.5,6.);
                \\draw [line width=2.pt,color=ccccff] (3.,6.)-- (4.,6.);
                \\draw [line width=2.pt,color=ccccff] (4.,6.)-- (3.5,5.);
                \\draw [line width=2.pt,color=ccccff] (3.5,5.)-- (3.,6.);
                \\draw [line width=2.pt] (1.5,4.)-- (3.,4.);
                \\draw [line width=2.pt] (0.5,4.)-- (4.,4.);
                \\draw [line width=2.pt,color=ccccff] (1.5,4.)-- (0.5,4.);
                \\draw [line width=2.pt,color=ccccff] (3.,4.)-- (4.,4.);
                \\draw [line width=2.pt] (0.,5.)-- (0.5,6.);
                \\draw [line width=2.pt] (0.5,6.)-- (1.,5.);
                \\draw [line width=2.pt] (1.,5.)-- (0.5,4.);
                \\draw [line width=2.pt] (0.5,4.)-- (0.,5.);
                \\draw [line width=2.pt] (1.,5.)-- (1.5,6.);
                \\draw [line width=2.pt] (1.,5.)-- (1.5,4.);
                \\draw [line width=2.pt] (1.5,6.)-- (3.,6.);
                \\draw [line width=2.pt] (3.,6.)-- (3.5,5.);
                \\draw [line width=2.pt] (3.5,5.)-- (3.,4.);
                \\draw [line width=2.pt] (3.,4.)-- (1.5,4.);
                \\draw [line width=2.pt] (3.5,5.)-- (4.,6.);
                \\draw [line width=2.pt] (4.,6.)-- (4.5,5.);
                \\draw [line width=2.pt] (4.5,5.)-- (4.,4.);
                \\draw [line width=2.pt] (4.,4.)-- (3.5,5.);
                \\draw [line width=2.pt] (0.5,6.)-- (4.,6.);
                \\draw [line width=2.pt] (0.5,4.)-- (4.,4.);
                \\draw [line width=2.pt,color=wwqqzz] (0.5,6.)-- (1.,7.);
                \\draw [line width=2.pt,color=wwqqzz] (1.,7.)-- (1.5,6.);
                \\draw [line width=2.pt,color=wwqqzz] (1.5,6.)-- (0.5,6.);
                \\draw [line width=2.pt,color=wwqqzz] (3.,6.)-- (3.5,7.);
                \\draw [line width=2.pt,color=wwqqzz] (3.5,7.)-- (4.,6.);
                \\draw [line width=2.pt,color=wwqqzz] (4.,6.)-- (3.,6.);
                \\draw [line width=2.pt,color=zzwwff] (0.5,8.)-- (0.,7.);
                \\draw [line width=2.pt,color=zzwwff] (0.,7.)-- (0.5,6.);
                \\draw [line width=2.pt,color=zzwwff] (0.5,6.)-- (1.,7.);
                \\draw [line width=2.pt,color=zzwwff] (1.,7.)-- (0.5,8.);
                \\draw [line width=2.pt,color=zzwwff] (4.,8.)-- (3.5,7.);
                \\draw [line width=2.pt,color=zzwwff] (3.5,7.)-- (4.,6.);
                \\draw [line width=2.pt,color=zzwwff] (4.,6.)-- (4.5,7.);
                \\draw [line width=2.pt,color=zzwwff] (4.5,7.)-- (4.,8.);
                \\draw [line width=2.pt,color=ccccff] (0.5,8.)-- (1.,7.);
                \\draw [line width=2.pt,color=ccccff] (1.,7.)-- (1.5,8.);
                \\draw [line width=2.pt,color=ccccff] (1.5,8.)-- (0.5,8.);
                \\draw [line width=2.pt,color=ccccff] (3.,8.)-- (4.,8.);
                \\draw [line width=2.pt,color=ccccff] (4.,8.)-- (3.5,7.);
                \\draw [line width=2.pt,color=ccccff] (3.5,7.)-- (3.,8.);
                \\draw [line width=2.pt,color=ccccff] (1.5,6.)-- (0.5,6.);
                \\draw [line width=2.pt,color=ccccff] (3.,6.)-- (4.,6.);
                \\draw [line width=2.pt] (1.5,6.)-- (3.,6.);
                \\draw [line width=2.pt] (0.5,6.)-- (4.,6.);
                \\draw [line width=2.pt] (1.5,6.)-- (3.,6.);
                \\draw [line width=2.pt] (0.5,6.)-- (4.,6.);
                \\draw [line width=2.pt,color=ccccff] (1.5,6.)-- (0.5,6.);
                \\draw [line width=2.pt,color=ccccff] (3.,6.)-- (4.,6.);
                \\draw [line width=2.pt] (0.,7.)-- (0.5,8.);
                \\draw [line width=2.pt] (0.5,8.)-- (1.,7.);
                \\draw [line width=2.pt] (1.,7.)-- (0.5,6.);
                \\draw [line width=2.pt] (0.5,6.)-- (0.,7.);
                \\draw [line width=2.pt] (1.,7.)-- (1.5,8.);
                \\draw [line width=2.pt] (1.,7.)-- (1.5,6.);
                \\draw [line width=2.pt] (1.5,8.)-- (3.,8.);
                \\draw [line width=2.pt] (3.,8.)-- (3.5,7.);
                \\draw [line width=2.pt] (3.5,7.)-- (3.,6.);
                \\draw [line width=2.pt] (3.,6.)-- (1.5,6.);
                \\draw [line width=2.pt] (3.5,7.)-- (4.,8.);
                \\draw [line width=2.pt] (4.,8.)-- (4.5,7.);
                \\draw [line width=2.pt] (4.5,7.)-- (4.,6.);
                \\draw [line width=2.pt] (4.,6.)-- (3.5,7.);
                \\draw [line width=2.pt] (0.5,8.)-- (4.,8.);
                \\draw [line width=2.pt] (0.5,6.)-- (4.,6.);
                \\draw [line width=2.pt,color=wwqqzz] (0.5,8.)-- (1.,9.);
                \\draw [line width=2.pt,color=wwqqzz] (1.,9.)-- (1.5,8.);
                \\draw [line width=2.pt,color=wwqqzz] (1.5,8.)-- (0.5,8.);
                \\draw [line width=2.pt,color=wwqqzz] (3.,8.)-- (3.5,9.);
                \\draw [line width=2.pt,color=wwqqzz] (3.5,9.)-- (4.,8.);
                \\draw [line width=2.pt,color=wwqqzz] (4.,8.)-- (3.,8.);
                \\draw [line width=2.pt,color=zzwwff] (0.5,10.)-- (0.,9.);
                \\draw [line width=2.pt,color=zzwwff] (0.,9.)-- (0.5,8.);
                \\draw [line width=2.pt,color=zzwwff] (0.5,8.)-- (1.,9.);
                \\draw [line width=2.pt,color=zzwwff] (1.,9.)-- (0.5,10.);
                \\draw [line width=2.pt,color=zzwwff] (4.,10.)-- (3.5,9.);
                \\draw [line width=2.pt,color=zzwwff] (3.5,9.)-- (4.,8.);
                \\draw [line width=2.pt,color=zzwwff] (4.,8.)-- (4.5,9.);
                \\draw [line width=2.pt,color=zzwwff] (4.5,9.)-- (4.,10.);
                \\draw [line width=2.pt,color=ccccff] (0.5,10.)-- (1.,9.);
                \\draw [line width=2.pt,color=ccccff] (1.,9.)-- (1.5,10.);
                \\draw [line width=2.pt,color=ccccff] (1.5,10.)-- (0.5,10.);
                \\draw [line width=2.pt,color=ccccff] (3.,10.)-- (4.,10.);
                \\draw [line width=2.pt,color=ccccff] (4.,10.)-- (3.5,9.);
                \\draw [line width=2.pt,color=ccccff] (3.5,9.)-- (3.,10.);
                \\draw [line width=2.pt,color=ccccff] (1.5,8.)-- (0.5,8.);
                \\draw [line width=2.pt,color=ccccff] (3.,8.)-- (4.,8.);
                \\draw [line width=2.pt] (1.5,8.)-- (3.,8.);
                \\draw [line width=2.pt] (0.5,8.)-- (4.,8.);
                \\draw [line width=2.pt,color=ccccff] (1.5,8.)-- (0.5,8.);
                \\draw [line width=2.pt,color=ccccff] (3.,8.)-- (4.,8.);
                \\draw [line width=2.pt] (1.5,8.)-- (3.,8.);
                \\draw [line width=2.pt] (0.5,8.)-- (4.,8.);
                \\draw [line width=2.pt] (1.5,8.)-- (3.,8.);
                \\draw [line width=2.pt] (0.5,8.)-- (4.,8.);
                \\draw [line width=2.pt,color=ccccff] (1.5,8.)-- (0.5,8.);
                \\draw [line width=2.pt,color=ccccff] (3.,8.)-- (4.,8.);
                \\draw [line width=2.pt] (0.,9.)-- (0.5,10.);
                \\draw [line width=2.pt] (0.5,10.)-- (1.,9.);
                \\draw [line width=2.pt] (1.,9.)-- (0.5,8.);
                \\draw [line width=2.pt] (0.5,8.)-- (0.,9.);
                \\draw [line width=2.pt] (1.,9.)-- (1.5,10.);
                \\draw [line width=2.pt] (1.,9.)-- (1.5,8.);
                \\draw [line width=2.pt] (1.5,10.)-- (3.,10.);
                \\draw [line width=2.pt] (3.,10.)-- (3.5,9.);
                \\draw [line width=2.pt] (3.5,9.)-- (3.,8.);
                \\draw [line width=2.pt] (3.,8.)-- (1.5,8.);
                \\draw [line width=2.pt] (3.5,9.)-- (4.,10.);
                \\draw [line width=2.pt] (4.,10.)-- (4.5,9.);
                \\draw [line width=2.pt] (4.5,9.)-- (4.,8.);
                \\draw [line width=2.pt] (4.,8.)-- (3.5,9.);
                \\draw [line width=2.pt] (0.5,10.)-- (4.,10.);
                \\draw [line width=2.pt] (0.5,8.)-- (4.,8.);
                \\draw [line width=2.pt,color=wwqqzz] (0.5,10.)-- (1.,11.);
                \\draw [line width=2.pt,color=wwqqzz] (1.,11.)-- (1.5,10.);
                \\draw [line width=2.pt,color=wwqqzz] (1.5,10.)-- (0.5,10.);
                \\draw [line width=2.pt,color=wwqqzz] (3.,10.)-- (3.5,11.);
                \\draw [line width=2.pt,color=wwqqzz] (3.5,11.)-- (4.,10.);
                \\draw [line width=2.pt,color=wwqqzz] (4.,10.)-- (3.,10.);
                \\draw [line width=2.pt,color=zzwwff] (0.5,12.)-- (0.,11.);
                \\draw [line width=2.pt,color=zzwwff] (0.,11.)-- (0.5,10.);
                \\draw [line width=2.pt,color=zzwwff] (0.5,10.)-- (1.,11.);
                \\draw [line width=2.pt,color=zzwwff] (1.,11.)-- (0.5,12.);
                \\draw [line width=2.pt,color=zzwwff] (4.,12.)-- (3.5,11.);
                \\draw [line width=2.pt,color=zzwwff] (3.5,11.)-- (4.,10.);
                \\draw [line width=2.pt,color=zzwwff] (4.,10.)-- (4.5,11.);
                \\draw [line width=2.pt,color=zzwwff] (4.5,11.)-- (4.,12.);
                \\draw [line width=2.pt,color=ccccff] (0.5,12.)-- (1.,11.);
                \\draw [line width=2.pt,color=ccccff] (1.,11.)-- (1.5,12.);
                \\draw [line width=2.pt,color=ccccff] (1.5,12.)-- (0.5,12.);
                \\draw [line width=2.pt,color=ccccff] (3.,12.)-- (4.,12.);
                \\draw [line width=2.pt,color=ccccff] (4.,12.)-- (3.5,11.);
                \\draw [line width=2.pt,color=ccccff] (3.5,11.)-- (3.,12.);
                \\draw [line width=2.pt,color=ccccff] (1.5,10.)-- (0.5,10.);
                \\draw [line width=2.pt,color=ccccff] (3.,10.)-- (4.,10.);
                \\draw [line width=2.pt] (1.5,10.)-- (3.,10.);
                \\draw [line width=2.pt] (0.5,10.)-- (4.,10.);
                \\draw [line width=2.pt,color=ccccff] (1.5,10.)-- (0.5,10.);
                \\draw [line width=2.pt,color=ccccff] (3.,10.)-- (4.,10.);
                \\draw [line width=2.pt] (1.5,10.)-- (3.,10.);
                \\draw [line width=2.pt] (0.5,10.)-- (4.,10.);
                \\draw [line width=2.pt,color=ccccff] (1.5,10.)-- (0.5,10.);
                \\draw [line width=2.pt,color=ccccff] (3.,10.)-- (4.,10.);
                \\draw [line width=2.pt] (1.5,10.)-- (3.,10.);
                \\draw [line width=2.pt] (0.5,10.)-- (4.,10.);
                \\draw [line width=2.pt] (1.5,10.)-- (3.,10.);
                \\draw [line width=2.pt] (0.5,10.)-- (4.,10.);
                \\draw [line width=2.pt,color=ccccff] (1.5,10.)-- (0.5,10.);
                \\draw [line width=2.pt,color=ccccff] (3.,10.)-- (4.,10.);
                \\draw [line width=2.pt] (0.,11.)-- (0.5,12.);
                \\draw [line width=2.pt] (0.5,12.)-- (1.,11.);
                \\draw [line width=2.pt] (1.,11.)-- (0.5,10.);
                \\draw [line width=2.pt] (0.5,10.)-- (0.,11.);
                \\draw [line width=2.pt] (1.,11.)-- (1.5,12.);
                \\draw [line width=2.pt] (1.,11.)-- (1.5,10.);
                \\draw [line width=2.pt] (1.5,12.)-- (3.,12.);
                \\draw [line width=2.pt] (3.,12.)-- (3.5,11.);
                \\draw [line width=2.pt] (3.5,11.)-- (3.,10.);
                \\draw [line width=2.pt] (3.,10.)-- (1.5,10.);
                \\draw [line width=2.pt] (3.5,11.)-- (4.,12.);
                \\draw [line width=2.pt] (4.,12.)-- (4.5,11.);
                \\draw [line width=2.pt] (4.5,11.)-- (4.,10.);
                \\draw [line width=2.pt] (4.,10.)-- (3.5,11.);
                \\draw [line width=2.pt] (0.5,12.)-- (4.,12.);
                \\draw [line width=2.pt] (0.5,10.)-- (4.,10.);
                \\draw [line width=2.pt,color=wwqqzz] (0.5,12.)-- (1.,13.);
                \\draw [line width=2.pt,color=wwqqzz] (1.,13.)-- (1.5,12.);
                \\draw [line width=2.pt,color=wwqqzz] (1.5,12.)-- (0.5,12.);
                \\draw [line width=2.pt,color=wwqqzz] (3.,12.)-- (3.5,13.);
                \\draw [line width=2.pt,color=wwqqzz] (3.5,13.)-- (4.,12.);
                \\draw [line width=2.pt,color=wwqqzz] (4.,12.)-- (3.,12.);
                \\draw [line width=2.pt,color=zzwwff] (0.5,14.)-- (0.,13.);
                \\draw [line width=2.pt,color=zzwwff] (0.,13.)-- (0.5,12.);
                \\draw [line width=2.pt,color=zzwwff] (0.5,12.)-- (1.,13.);
                \\draw [line width=2.pt,color=zzwwff] (1.,13.)-- (0.5,14.);
                \\draw [line width=2.pt,color=zzwwff] (4.,14.)-- (3.5,13.);
                \\draw [line width=2.pt,color=zzwwff] (3.5,13.)-- (4.,12.);
                \\draw [line width=2.pt,color=zzwwff] (4.,12.)-- (4.5,13.);
                \\draw [line width=2.pt,color=zzwwff] (4.5,13.)-- (4.,14.);
                \\draw [line width=2.pt,color=ccccff] (0.5,14.)-- (1.,13.);
                \\draw [line width=2.pt,color=ccccff] (1.,13.)-- (1.5,14.);
                \\draw [line width=2.pt,color=ccccff] (1.5,14.)-- (0.5,14.);
                \\draw [line width=2.pt,color=ccccff] (3.,14.)-- (4.,14.);
                \\draw [line width=2.pt,color=ccccff] (4.,14.)-- (3.5,13.);
                \\draw [line width=2.pt,color=ccccff] (3.5,13.)-- (3.,14.);
                \\draw [line width=2.pt,color=ccccff] (1.5,12.)-- (0.5,12.);
                \\draw [line width=2.pt,color=ccccff] (3.,12.)-- (4.,12.);
                \\draw [line width=2.pt] (1.5,12.)-- (3.,12.);
                \\draw [line width=2.pt] (0.5,12.)-- (4.,12.);
                \\draw [line width=2.pt,color=ccccff] (1.5,12.)-- (0.5,12.);
                \\draw [line width=2.pt,color=ccccff] (3.,12.)-- (4.,12.);
                \\draw [line width=2.pt] (1.5,12.)-- (3.,12.);
                \\draw [line width=2.pt] (0.5,12.)-- (4.,12.);
                \\draw [line width=2.pt,color=ccccff] (1.5,12.)-- (0.5,12.);
                \\draw [line width=2.pt,color=ccccff] (3.,12.)-- (4.,12.);
                \\draw [line width=2.pt] (1.5,12.)-- (3.,12.);
                \\draw [line width=2.pt] (0.5,12.)-- (4.,12.);
                \\draw [line width=2.pt,color=ccccff] (1.5,12.)-- (0.5,12.);
                \\draw [line width=2.pt,color=ccccff] (3.,12.)-- (4.,12.);
                \\draw [line width=2.pt] (1.5,12.)-- (3.,12.);
                \\draw [line width=2.pt] (0.5,12.)-- (4.,12.);
                \\draw [line width=2.pt] (1.5,12.)-- (3.,12.);
                \\draw [line width=2.pt] (0.5,12.)-- (4.,12.);
                \\draw [line width=2.pt,color=ccccff] (1.5,12.)-- (0.5,12.);
                \\draw [line width=2.pt,color=ccccff] (3.,12.)-- (4.,12.);
                \\draw [line width=2.pt] (0.,13.)-- (0.5,14.);
                \\draw [line width=2.pt] (0.5,14.)-- (1.,13.);
                \\draw [line width=2.pt] (1.,13.)-- (0.5,12.);
                \\draw [line width=2.pt] (0.5,12.)-- (0.,13.);
                \\draw [line width=2.pt] (1.,13.)-- (1.5,14.);
                \\draw [line width=2.pt] (1.,13.)-- (1.5,12.);
                \\draw [line width=2.pt] (1.5,14.)-- (3.,14.);
                \\draw [line width=2.pt] (3.,14.)-- (3.5,13.);
                \\draw [line width=2.pt] (3.5,13.)-- (3.,12.);
                \\draw [line width=2.pt] (3.,12.)-- (1.5,12.);
                \\draw [line width=2.pt] (3.5,13.)-- (4.,14.);
                \\draw [line width=2.pt] (4.,14.)-- (4.5,13.);
                \\draw [line width=2.pt] (4.5,13.)-- (4.,12.);
                \\draw [line width=2.pt] (4.,12.)-- (3.5,13.);
                \\draw [line width=2.pt] (0.5,14.)-- (4.,14.);
                \\draw [line width=2.pt] (0.5,12.)-- (4.,12.);

                \\node at (2.2,3) {\\textcolor{red}{\\fontsize{50pt}{16pt}\\selectfont\\textbf{1}}};
                \\node at (2.2,5) {\\textcolor{red}{\\fontsize{50pt}{16pt}\\selectfont\\textbf{2}}};
                \\node at (2.2,7) {\\textcolor{red}{\\fontsize{50pt}{16pt}\\selectfont\\textbf{3}}};
                \\node at (2.2,9) {\\textcolor{red}{\\fontsize{50pt}{16pt}\\selectfont\\textbf{4}}};
                \\node at (2.2,11) {\\textcolor{red}{\\fontsize{50pt}{16pt}\\selectfont\\textbf{5}}};
                \\node at (2.2,13) {\\textcolor{red}{\\fontsize{50pt}{16pt}\\selectfont\\textbf{6}}};

                \\node at (4.5,1) {\\textcolor{red}{\\fontsize{16pt}{16pt}\\selectfont\\textbf{Xuất phát}}};
                \\node at (5.5,13) {\\textcolor{red}{\\fontsize{16pt}{16pt}\\selectfont\\textbf{Đích}}};
            \\end{tikzpicture}
            \\scalebox{0.2}{ 
            \\begin{tikzpicture}[line cap=round,line join=round]
                \\path[fill] (0,0) .. controls +(-0.01,0.07) and +(0.04,-0.06) .. (-0.08,0.2) .. controls +(-0.07,0.1) and +(0.13,-0.01) .. (-0.4,0.38) .. controls +(-0.11,0) and +(0.11,-0) .. (-0.74,0.39) .. controls +(-0.07,0.17) and +(0.14,-0.13) .. (-1.07,0.84) .. controls +(-0.26,0.26) and +(0.33,-0.17) .. (-1.98,1.47) .. controls +(-0.04,0.03) and +(0.02,-0.04) .. (-2.06,1.58) .. controls +(-0.07,0.14) and +(0.01,-0.16) .. (-2.2,2.03) .. controls +(-0.03,0.23) and +(-0.14,-0.19) .. (-2.03,2.69) .. controls +(0.28,0) and +(-0.23,-0.2) .. (-1.27,2.86) .. controls +(0.06,0.07) and +(-0.01,-0.09) .. (-1.17,3.11) .. controls +(0.01,0.18) and +(0,-0.18) .. (-1.17,3.65) .. controls +(-0.01,0.43) and +(0.1,0) .. (-1.61,4.11) .. controls +(0.02,0) and +(-0.02,-0) .. (-1.55,4.12) .. controls +(0,0.36) and +(-0.09,-0.35) .. (-1.4,5.18) .. controls +(0.09,0.35) and +(-0.12,-0.34) .. (-1.08,6.21) .. controls +(0.1,0.32) and +(-0.1,-0.31) .. (-0.76,7.15) .. controls +(0.23,0.7) and +(-0.1,-0.73) .. (-0.23,9.29) .. controls +(0.14,0.96) and +(0.13,-0.69) .. (-0.27,11.77) .. controls +(-0.23,1.38) and +(0.95,-1.02) .. (-2.04,15.39) .. controls +(-0.45,0.47) and +(0.57,-0.32) .. (-3.59,16.58 ) .. controls +(-0.67,0.37) and +(0.76,-0.1) .. (-5.75,17.3) .. controls +(0.09,-0.05) and +(-0.09,0.05) .. (-5.49,17.15) .. controls +(0.53,-0.3) and +(-0.49,0.36) .. (-3.95,16.16) .. controls +(0.89,-0.62) and +(-0.76,1.95) .. (-1.27,12.76) .. controls +(0.12,-0.3) and +(-0.05,0.32) .. (-1.01,11.84) .. controls +(0.03,-0.19) and +(-0.02,0.2) .. (-0.93,11.26) .. controls +(0,-0.05) and +(0,0.05) .. (-0.92,11.12) .. controls +(-0.04,0.16) and +(0.04,-0.16) .. (-1.05,11.59) .. controls +(-0.46,1.54) and +(2.31,-0.83) .. (-5.04,16.31) .. controls +(-0.16,0.06) and +(0.17,-0.04) .. (-5.52,16.45) .. controls +(0.13,0.04) and +(-0.13,-0.04) .. (-5.13,16.57) .. controls +(-0.1,0.09) and +(0.11,-0.08 ) .. (-5.44,16.83) .. controls +(-0.86,0.64) and +(0.62,-0.35) .. (-7.48,18.15) .. controls +(-0.03,-0.09) and +(-0.38,0.63) .. (-7.2,16.32) .. controls +(0.27,0.11) and +(-0.29,-0.01) .. (-6.34,16.48 ) .. controls +(-0.58,-0.22) and +(0.5,0.37) .. (-7.99,15.61) .. controls +(-0.13,-0.1) and +(0.12,0.11) .. (-8.37,15.31) .. controls +(-0.01,-0.02) and +(0.01,-0) .. (-8.42,15.3) .. controls +(-0.16,0.03) and +(0.14,0.07) .. (-8.88,15.23) .. controls +(-0.04,-0.02) and +(0.03,0.05) .. (-9.01,15.13) .. controls +(-0.15,-0.29) and +(0.05,0.31) .. (-9.21,14.19) .. controls +(-0.01,-0.04) and +(0.03,0.04) .. (-9.26,14.06) .. controls +(-0.58,-0.72) and +(0.5,0.79) .. (-10.91,11.82) .. controls +(-0.08,-0.13) and +(0.09,0.13) .. (-11.17,11.42) .. controls +(-0.07,-0.1) and +(0.03,0.13) .. (-11.34,11.08 ) .. controls +(-0.03,-0.12) and +(-0.04,0.11) .. (-11.34,10.72) .. controls +(0.07,-0.23) and +(-0.17,0.18 ) .. (-10.98,10.09) .. controls +(0.1,-0.11) and +(-0.14,0.08 ) .. (-10.62,9.8 ) .. controls +(0.04,-0.03) and +(-0.04,0.03) .. (-10.48,9.72) .. controls +(0.22,-0.08 ) and +(-0.07,0) .. (-9.85,9.63) .. controls +(0.1,0.15) and +(-0.12,-0.14) .. (-9.51,10.06) .. controls +(0.22,0.25) and +(-0.25,-0.22) .. (-8.79,10.76) .. controls +(0.02,0.03) and +(-0.03,0) .. (-8.7,10.77) .. controls +(0.5,-0.02) and +(-0.49,-0.12) .. (-7.19,10.88 ) .. controls +(0.39,0.09) and +(-0.31,-0.26) .. (-6.12,11.4) .. controls +(0.14,0.12) and +(-0.11,-0.15) .. (-5.75,11.81) .. controls +(-0,-0.04) and +(0.02,0.03) .. (-5.77,11.7) .. controls +(-0.01,-0.03) and +(0,0.04) .. (-5.82,11.61) .. controls +(-0.03,-0.34) and +(0.14,0.31) .. (-6.08,10.63) .. controls +(-0.3,-0.7) and +(0.77,0.83) .. (-7.68,8.33) .. controls +(-0.65,-0.65) and +(0.44,0.83) .. (-9.34,6.21) .. controls +(-0.32,-0.63) and +(0.04,0.71) .. (-9.91,4.18 ) .. controls +(0,-0.02) and +(0,0.02) .. (-9.91,4.11) .. controls +(-0.07,0) and +(0.07,0.01) .. (-10.14,4.1) .. controls +(-0.15,-0.03) and +(0,0.34) .. (-10.54,3.72) .. controls +(-0,-0.04) and +(-0.03,0.13) .. (-10.54,3.06) .. controls +(0.04,-0.18 ) and +(-0.26,0.03) .. (-10.09,2.7) .. controls +(0.1,-0.01) and +(-0.1,0.01) .. (-9.79,2.69) .. controls +(0.1,-0.11) and +(-0.02,0.14) .. (-9.6,2.3) .. controls +(0.03,-0.2) and +(0.07,0.19) .. (-9.67,1.72) .. controls +(-0.04,-0.08 ) and +(0.05,0.03) .. (-9.82,1.48 ) .. controls +(-0.28,-0.14) and +(0.24,0.2) .. (-10.61,0.98 ) .. controls +(-0.2,-0.17) and +(0.1,0.24) .. (-11.09,0.38 ) .. controls +(-0.36,-0.02) and +(0.09,0.36) .. (-11.74,-0.13) -- (-11.74,-1.21) .. controls +(3.92,0) and +(-3.92,0) .. (0.01,-1.21) .. controls +(0,0.43) and +(0.01,-0.41) .. (0,0) -- cycle (-0.92,11.11) .. controls +(0.01,0) and +(0.01,0.01) .. (-0.91,11.09) .. controls +(-0.01,-0) and +(-0.01,-0) .. (-0.92,11.11) -- cycle (-4.32,3.08 ) .. controls +(0.94,0.03) and +(-0.07,0.02) .. (-1.44,3.08 ) .. controls +(-0.89,-0.03) and +(0.08,-0.03) .. (-4.32,3.08 ) -- cycle (-7.71,13.47) .. controls +(0.07,0.01) and +(-0.06,0.03) .. (-7.5,13.44) .. controls +(0.07,-0.04) and +(0,0.08 ) .. (-7.39,13.26) .. controls +(0.02,-0.22) and +(0.37,-0.04) .. (-8.03,12.88 ) .. controls +(-0.17,0.01) and +(0.16,0.04) .. (-8.53,12.85) .. controls +(0.04,0.06) and +(-0.04,-0.05) .. (-8.4,13.01) .. controls +(0.14,0.15) and +(-0.28,-0.04) .. (-7.71,13.47) -- cycle (-8.6,14.62) .. controls +(0.03,0.07) and +(-0.07,0.01) .. (-8.43,14.68 ) .. controls +(0.14,-0.03) and +(-0.13,0.06) .. (-8.02,14.53) .. controls +(-0.14,-0.08 ) and +(0.08,-0.2) .. (-8.62,14.49) .. controls +(-0.01,0.04) and +(-0.02,-0.04) .. (-8.6,14.62) -- cycle (-6.07,11.88 ) .. controls +(-0.33,-0.34) and +(0.33,0.1) .. (-7.13,11.3) .. controls +(-0.44,-0.15) and +(0.46,0.01) .. (-8.49,11.14) .. controls +(-0.16,-0) and +(0.15,0.07) .. (-8.96,11.06) .. controls +(-0.1,-0.04) and +(0.07,0.07) .. (-9.21,10.88 ) .. controls +(-0.18,-0.17) and +(0.18,0.17) .. (-9.74,10.33) .. controls +(-0.14,-0.13) and +(0.19,0.03) .. (-10.22,10.06) .. controls +(-0.08,-0.02) and +(0.08,-0.02) .. (-10.47,10.07) .. controls +(-0.04,0.01) and +(0.03,-0.02) .. (-10.58,10.12) .. controls +(0.04,-0.01) and +(-0.04,0) .. (-10.46,10.08 ) .. controls +(0.12,-0.01) and +(-0.1,-0.06) .. (-10.14,10.19) .. controls +(0.18,0.12) and +(-0.15,-0.16) .. (-9.66,10.63) .. controls +(0.16,0.17) and +(-0.17,-0.15) .. (-9.17,11.12) .. controls +(0.04,0.03) and +(-0.04,-0.03) .. (-9.06,11.21) .. controls +(0.08,0.06) and +(-0.09,-0.02) .. (-8.8,11.32) .. controls +(0.26,0.03) and +(-0.26,0) .. (-8.01,11.36) .. controls +(0.22,0.01) and +(-0.21,-0.05) .. (-7.37,11.45) .. controls +(0.45,0.1) and +(-0.35,-0.32) .. (-6.12,12.04) .. controls +(0.15,0.14) and +(-0.09,-0.19) .. (-5.75,12.53) .. controls +(0.11,0.22) and +(-0.03,-0.25) .. (-5.56,13.24) .. controls +(0.01,-0.07) and +(0.01,0.07) .. (-5.56,13.04) .. controls +(-0.03,-0.43) and +(0.31,0.31) .. (-6.07,11.88 ) -- cycle (-8.67,6.44) .. controls +(0.28,0.53) and +(-0.42,-0.42) .. (-7.62,7.87) .. controls +(1,0.94) and +(-0.7,-1.2) .. (-4.84,10.94) .. controls +(0.14,0.25) and +(-0.05,-0.28 ) .. (-4.52,11.73) .. controls +(-0.02,-0.35) and +(0.14,0.32) .. (-4.77,10.71) .. controls +(-0.73,-1.66) and +(0.83,1.63) .. (-8.23,6.48 ) .. controls +(-0.15,-0.29) and +(0.09,0.32) .. (-8.59,5.57) .. controls +(-0.1,-0.34) and +(0.04,0.36) .. (-8.8,4.51) .. controls +(0,-0.01) and +(0,0.01) .. (-8.81,4.47) .. controls +(-0.16,0) and +(0.16,-0) .. (-9.29,4.47) .. controls +(0.1,0.69) and +(-0.32,-0.61) .. (-8.67,6.44) -- cycle (-9.74,3.61) .. controls +(-0.07,0) and +(-0.01,-0.08 ) .. (-9.88,3.73) .. controls +(-0.01,0) and +(0.01,0) .. (-9.92,3.74) .. controls +(0.02,0.15) and +(-0.29,-0.04) .. (-9.49,4.11) .. controls +(0.49,0.02) and +(-0.49,0) .. (-8.03,4.12) .. controls +(-0.18,-0.03) and +(0.08,0.18 ) .. (-8.46,3.83) .. controls +(0.32,0) and +(-0.3,-0.01) .. (-4.34,3.83) .. controls +(-0.08,0.18 ) and +(0.19,-0.01) .. (-4.8,4.11) .. controls +(0.09,0.01) and +(-0.09,0) .. (-4.53,4.11) .. controls +(0.88,-0.09) and +(-0.62,0.04) .. (-1.86,4.1) .. controls +(0.29,-0.05) and +(-0.01,0.14) .. (-1.44,3.73) .. controls +(-0,0) and +(0,-0) .. (-1.45,3.73) -- (-1.46,3.73) .. controls +(0.01,-0.05) and +(0.04,0.02) .. (-1.53,3.62) .. controls +(-0.83,-0.02) and +(0.87,0) .. (-4.15,3.61) .. controls +(-1.87,0) and +(1.86,-0) .. (-9.74,3.61) -- cycle (-9.28,2.5) .. controls +(-0.02,0.07) and +(0.04,-0.07) .. (-9.37,2.71) .. controls +(0.16,0) and +(-0.16,0) .. (-8.89,2.71) .. controls +(0.08,-0.15) and +(-0.02,0.17) .. (-8.73,2.22) .. controls +(0.03,-0.26) and +(0.11,0.23) .. (-8.87,1.48 ) .. controls +(-0.16,-0) and +(0.16,0) .. (-9.35,1.48 ) .. controls +(0.07,0.15) and +(-0.02,-0.16) .. (-9.21,1.94) .. controls +(0.02,0.19) and +(0,0) .. (-9.28,2.5) -- cycle (-0.4,-0.1) .. controls +(-0.04,-0.05) and +(0.06,0) .. (-0.57,-0.17) .. controls +(-3.4,0) and +(3.4,-0) .. (-10.78,-0.17) .. controls +(-0.07,0) and +(0.04,-0.05) .. (-10.95,-0.09) -- (-10.96,-0.09) .. controls +(0,0.03) and +(-0.01,-0.02) .. (-10.94,-0.01) .. controls +(0.04,0.17) and +(-0.33,-0.03) .. (-10.38,0.39) .. controls +(0.77,0.01) and +(-0.04,0.01) .. (-8.02,0.39) .. controls +(-0.13,-0.01) and +(0.11,0.08 ) .. (-8.4,0.25) .. controls +(-0.07,-0.05) and +(0.04,0.08 ) .. (-8.56,0.06) -- (-8.55,0.06) .. controls +(1.51,0) and +(-1.51,0) .. (-4.02,0.06) -- (-4.01,0.06) .. controls +(-0.11,0.23) and +(0.17,-0.02) .. (-4.54,0.38 ) .. controls +(0.04,0.01) and +(-0.04,-0) .. (-4.4,0.38 ) -- (-1.19,0.38 ) .. controls +(0.1,-0) and +(-0.1,0.02) .. (-0.89,0.37) .. controls +(0.19,-0.03) and +(-0.09,0.17) .. (-0.43,0.07) .. controls +(0.01,-0.03) and +(0.01,0.03) .. (-0.41,-0.01) .. controls +(0.01,-0.02) and +(-0,0.03) .. (-0.38,-0.09) .. controls +(-0.01,0) and +(0.01,0) .. (-0.4,-0.1) -- cycle;
                \\path[fill] (-7.34,16.31) .. controls +(-0.21,-0.1) and +(0.2,0.11) .. (-7.95,15.99) .. controls +(-0.18,0.28 ) and +(0.17,-0.32) .. (-8.47,16.89) .. controls +(0.26,0.21) and +(-0.22,-0.02) .. (-7.66,17.25) .. controls +(0.03,-0.35) and +(-0.19,0.28 ) .. (-7.34,16.31) -- cycle;
            \\end{tikzpicture}} }}'''                 
                            %(
                                ))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Xác suất để con ngựa về đích ở lần gieo thứ nhất bằng $\\frac{1}{6}$'
            nb_da_1_s = 'Xác suất để con ngựa về đích ở lần gieo thứ nhất bằng $\\frac{1}{3}$'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Gọi $A$ là biến cố "Con ngựa về đích ở lần gieo thứ nhất", khi đó \\\\
                            Số phần tử của không gian mẫu là $n(\\Omega)=6$. \\\\
                            $n(A)=1$ suy ra $P(A)=\\frac{1}{6}$.'''
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Xác suất để con ngựa về đích ở lần gieo thứ hai bằng $\\frac{5}{36}$'
            th_da_1_s = 'Xác suất để con ngựa về đích ở lần gieo thứ hai bằng $\\frac{5}{12}$' 
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Gọi $B$ là biến cố "Con ngựa về đích ở lần gieo thứ hai", khi đó \\\\
                            Số phần tử của không gian mẫu là $n(\\Omega)=6 \\cdot 6=36$. \\\\
                            $B=\\left \\lbrace (1;5), (2;4), (3;3), (4;2), (5;1) \\right \\rbrace$. \\\\
                            $n(B)=5$ suy ra $P(B)=\\frac{5}{36}$.'''
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Xác suất để con ngựa về đích ở lần gieo thứ ba và cả ba lần gieo con ngựa đều được di chuyển bằng $\\frac{5}{108}$' 
            vd_da_1_s = 'Xác suất để con ngựa về đích ở lần gieo thứ ba và cả ba lần gieo con ngựa đều được di chuyển bằng $\\frac{7}{108}$' 
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Gọi $C$ là biến cố "Con ngựa về đích ở lần gieo thứ ba và cả ba lần gieo con ngựa đều được di chuyển", khi đó \\\\
                            Số phần tử của không gian mẫu là $n(\\Omega)=6 \\cdot 6 \\cdot 6=216$. \\\\
                            Bộ ba số có tổng bằng $6$ gồm: \\\\
                                $(1;2;3)$ có $3!=6$ cách. \\\\
                                $(1;1;4)$ có $\\frac{3!}{2!}=3$ cách. \\\\
                                $(2;2;2) có $1$ cách$. \\\\
                            $n(C)=10$ suy ra $P(C)=\\frac{10}{216}=\\frac{5}{108}$.'''
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Xác suất để con ngựa về đích sau ba lần gieo bằng $\\frac{25}{216}$'
            vdc_da_1_s = 'Xác suất để con ngựa về đích sau ba lần gieo bằng $\\frac{19}{54}$'
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Gọi $D$ là biến cố "Con ngựa về đích sau nhiều nhất ba lần gieo", khi đó \\\\
                            Số phần tử của không gian mẫu là $n(\\Omega)=6 \\cdot 6 \\cdot 6=216$. \\\\
                            TH1: Ba lần gieo ngựa đều được đi là $P(C)=\\frac{5}{108}$. \\\\
                            TH2: Ba lần gieo có hai lần đứng yên (giả sử kết quả lần thứ nhất là $a$, lần thứ hai là $b$ với $a+b>6$). \\\\
                                $a=1; b=6$ có $1$ cách. \\\\
                                $a=2; b=\\left \\lbrace 5;6 \\right \\rbrace$ có $2$ cách. \\\\
                                $a=3; b=\\left \\lbrace 4;5;6 \\right \\rbrace$ có $3$ cách. \\\\
                                $a=4; b=\\left \\lbrace 3;4;5;6 \\right \\rbrace$ có $4$ cách. \\\\
                                $a=5; b=\\left \\lbrace 2;3;4;5;6 \\right \\rbrace$ có $5$ cách. \\\\
                            Suy ra số phần tử của ba lần gieo có hai lần đứng yên là $15$ và xác suất là $\\frac{15}{216}$. \\\\
                            Vậy $P(D)=\\frac{5}{108}+\\frac{15}{216}=\\frac{25}{216}$.'''
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)



            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

